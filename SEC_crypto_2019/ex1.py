#!/usr/bin/python3
import base64
import sys
import codecs

if len(sys.argv) == 2:
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        sys.exit(84)
    cont = f.readline()
    if (cont[-1] == '\n'):
        new = cont[:-1]
    f.close()
    if (len(cont) == 0):
        sys.exit(84)
    first = bytearray(bytes.fromhex(new))
    last = base64.b64encode(first).decode()
    print (last)
    sys.exit(0)
else:
    sys.exit(84)
