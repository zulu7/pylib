#!/usr/bin/env python

from Crypto import Random
from M2Crypto import EVP

from io_helper import stream

from padding import pad_pkcs5, unpad_pkcs5
from chunk_buffer import ChunkBuffer

ALGORITHM = 'aes_256_cbc'

# AES has a fixed block size of 16 bytes regardless of key size
BLOCK_SIZE = 16

ENC=1
DEC=0

def encrypt(in_file, out_file, key, iv, pad=True, chunk_size=stream.DEFAULT_CHUNK_SIZE, alg=ALGORITHM):
  cipher = EVP.Cipher(alg=alg, key=key, iv=iv, op=ENC)
  size = 0
  for chunk in stream.chunk_iter(in_file):
    out_file.write(cipher.update(chunk))
    size += len(chunk)
  if pad:
    padding = pad_pkcs5(size, BLOCK_SIZE)
    out_file.write(cipher.update(padding))
  out_file.write(cipher.final())

def decrypt(in_file, out_file, key, iv, unpad=True, chunk_size=stream.DEFAULT_CHUNK_SIZE):
  cipher = EVP.Cipher(alg=ALGORITHM, key=key, iv=iv, op=DEC)
  buf = ChunkBuffer(
    min_size=BLOCK_SIZE,
    evict_fn=lambda chunk: out_file.write(chunk)
    )
  for chunk in stream.chunk_iter(in_file):
    buf.append(cipher.update(chunk))
  buf.append(cipher.final())
  remainder = buf.getvalue()
  if unpad:
    out_file.write(unpad_pkcs5(remainder))
  else:
    out_file.write(remainder)

