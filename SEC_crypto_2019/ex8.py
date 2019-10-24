#!/usr/bin/python3

import sys
import base64

from Crypto.Cipher import AES

def detect(ciphert):
    ciphert = [[c[i:i+16] for i in range(0, len(ciphert))] for c in ciphert]
    data = max(enumerate(ciphert), key=lambda x: sum(x[1].count(b) for b in x[1]))[0]
    print(data + 1)

if len(sys.argv) == 2:
    try:
        with open(sys.argv[1], 'r') as files:
            ciphert = [base64.b64decode(l) for l in files]
            if len(ciphert) == 0:
                sys.exit(84)
    except IOError:
        sys.exit(84)
    except ValueError:
        sys.exit(84)

    detect(ciphert)

    sys.exit(0)
else:
    sys.exit(84)
