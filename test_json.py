#!/usr/bin/env python

import os
import sys

from io_helper import json_file

test_file = 'test.file'
test_obj = {'test': 42}
json_file.save_json_file(test_file, test_obj)
success = (json_file.load_json_file(test_file) == test_obj)
print('OK' if success else 'FAIL')
sys.exit(os.EX_OK if success else os.EX_SOFTWARE)
