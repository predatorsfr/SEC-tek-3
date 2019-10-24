#!/usr/bin/env python3
import base64
import sys

tab_letter = {
    'e': .11431, 's': .05694, 'g': .01813,'b': .01342,
    'y': .01776, 'l': .03622, 'p': .01736, 'a': .07350, 'm': .02165,'w': .02124, 
    'o': .06756, 'n': .06074, 'r': .05388, 'c': .02503, ' ': .11700,
    'u': .02482, 'd': .03827, 'i': .05484, 'f': .02005, 'h': .05473, 't': .08150
}

def cast_xor(single_elem, val):
    ret = b''
    for byte in single_elem:
        ret += bytes([byte ^ val])
    total = sum([tab_letter.get(chr(byte), 0) for byte in ret.lower()])
    return total

if len(sys.argv) == 2:
    string = []
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        sys.exit(84)
    first = f.readline()
    if (first[-1] == '\n'):
        first = first[:-1]
    if (len(first) == 0):
        sys.exit(84)
    cont = first
    txt = bytes.fromhex(cont)
    for i in range(256):
        new_cont = cast_xor(txt, i)
        place = cast_xor(txt, i)
        info = {'place':place, 'answer': i}
        string.append(info)
    tab = sorted(string, key=lambda x: x['place'], reverse=True)[0]
    print(bytes([tab['answer']]).hex().upper())
#    print(tab['answer'])
else:
    sys.exit(84)
