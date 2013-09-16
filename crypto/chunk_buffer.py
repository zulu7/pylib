from cStringIO import StringIO
from collections import deque

class ChunkBuffer:
  def __init__(self, min_size, evict_fn):
    self.min_size = min_size
    self.data = deque()
    self.data_len = 0
    self.evict_fn = evict_fn

  def can_evict(self):
    return self.data_len > 0 and self.data_len - self.data[0][0] > self.min_size

  def evict(self):
    size, chunk = self.data.popleft()
    self.evict_fn(chunk)
    self.data_len -= size

  def append(self, chunk):
    size = len(chunk)
    self.data.append((size, chunk))
    self.data_len += size
    while self.can_evict():
      self.evict()

  def getvalue(self):
    buf = StringIO()
    for size, chunk in self.data:
      buf.write(chunk)
    return buf.getvalue()
