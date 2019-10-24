#!/usr/bin/env python3
import base64
import sys

def cast_to_hex(content):
    return int(content,base=16)

def xor(first,second):
    i = cast_to_hex(first)
    j = cast_to_hex(second)
    return hex(i ^ j)

if len(sys.argv) == 2:
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print(sys.argv[1])
        sys.exit(84)
    first = f.readline()
    if (first[-1] == '\n'):
        first = first[:-1]
    if (len(first) == 0):
        sys.exit(84)
    second = f.readline()
    if (second[-1] == '\n'):
        second = second[:-1]
    if (len(first) != len(second)):
        sys.exit(84)
    ret = xor(first,second)
    ret = ret[2:]
    print (ret.upper())
    sys.exit(0)
else:
    sys.exit(84)
