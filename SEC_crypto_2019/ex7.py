#!/usr/bin/python3

import sys
import base64
import re

from Crypto.Cipher import AES

def ecb_decrypt(cipher, key):
    crypt = AES.new(key, AES.MODE_ECB)
    text = crypt.decrypt(cipher)
    print(base64.b64encode(text[:-text[-1]]).decode())

if len(sys.argv) == 2:
    try:
        with open(sys.argv[1], 'r') as files:
            key = bytes.fromhex(re.sub(r'\s', '', files.readline()))
            cipher = base64.b64decode(''.join(files.read()))
            if len(key) == 0 or len(cipher) == 0:
                sys.exit(84)
            msg = ecb_decrypt(cipher, key)
            sys.exit(0)
    except IOError:
            sys.exit(84)
else:
            sys.exit(84)
