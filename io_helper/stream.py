
DEFAULT_CHUNK_SIZE = 8192

def chunk_iter(in_file, chunk_size=DEFAULT_CHUNK_SIZE):
  while True:
    chunk = in_file.read(chunk_size)
    if not chunk:
      break
    yield chunk
