have_cjson = False
try:
  import cjson
  have_cjson = True
except ImportError:
  import json

def encode(obj):
  if have_cjson:
    return cjson.encode(obj)
  else:
    return json.dumps(obj)

def decode(string):
  if have_cjson:
    return cjson.decode(string)
  else:
    return json.loads(string)

def load_json_file(filename):
  with open(filename) as f:
    return decode(f.read())

def save_json_file(filename, obj):
  with open(filename, 'w') as f:
    f.write(encode(obj))
