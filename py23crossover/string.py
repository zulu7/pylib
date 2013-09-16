import sys

py2 = (sys.version[0] < '3')
string_base = basestring if py2 else str

