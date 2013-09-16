def pad_pkcs5(plaintext_size, block_size):
  padding_len = block_size - plaintext_size % block_size
  return padding_len * chr(padding_len)

def unpad_pkcs5(final_ciphertext):
  return final_ciphertext[0:-ord(final_ciphertext[-1])]
