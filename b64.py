#!/usr/bin/env python

import argparse
import base64
import sys

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-e', '--encode', action='store_true')
  parser.add_argument('-d', '--decode', action='store_true')
  parser.add_argument('-t', '--trim', action='store_true')
  args = parser.parse_args()

  str_in = sys.stdin.read()
  if args.trim:
    str_in = str_in.strip()

  if args.encode:
    print(base64.standard_b64encode(str_in))
  else:
    print(base64.standard_b64decode(str_in))

if __name__ == '__main__':
  sys.exit(main())
