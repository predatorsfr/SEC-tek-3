#!/usr/bin/env python3
import base64
import sys
import re

if len(sys.argv) == 2:
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print(sys.argv[1])
        sys.exit(84)
    first = re.sub(r'\s', '', f.readline())
    rest = ''.join(f.read())
    print (first)
    print (rest)
    if (first[-1] == '\n'):
        first = first[:-1]
    if (len(first) == 0):
        sys.exit(84)
    sys.exit(0)
else:
    sys.exit(84)
