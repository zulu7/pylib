def get_hex(data):
  return [x.encode('hex') for x in data]

def get_bytes(data):
  return ' '.join(get_hex(data))

def write_bytes(data):
  print(' '.join(get_hex(data)))
