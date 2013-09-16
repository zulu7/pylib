#!/usr/bin/env python

import argparse
import base64
import sys

from crypto import stream_crypto
from crypto.byte_util import get_bytes

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-k', '--key', default='bX/10noAkJ9QrUzRIP/vqIcYSHBsbiJafIWSixIGrOY=')
  parser.add_argument('-iv', '--iv', default=base64.standard_b64encode(stream_crypto.BLOCK_SIZE*'\0'))
  parser.add_argument('-d', '--decrypt', action='store_true')
  parser.add_argument('-e', '--encrypt', action='store_true')
  parser.add_argument('--no-pad', action='store_true')
  args = parser.parse_args()

  key = base64.standard_b64decode(args.key)
  iv = base64.standard_b64decode(args.iv)

  sys.stderr.write('key: %s\n' % get_bytes(key))
  sys.stderr.write('iv: %s\n' % get_bytes(iv))

  if args.encrypt:
    stream_crypto.encrypt(sys.stdin, sys.stdout, key=key, iv=iv, pad=not args.no_pad)
  else:
    stream_crypto.decrypt(sys.stdin, sys.stdout, key=key, iv=iv, unpad=not args.no_pad)

if __name__ == '__main__':
  sys.exit(main())
