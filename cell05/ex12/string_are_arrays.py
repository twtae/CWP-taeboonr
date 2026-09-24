#!/usr/bin/python3

import sys

if (len(sys.argv) != 2):
    print("none")
else:
    z_count = len([z for z in sys.argv[1] if z == 'z'])
    print('z' * z_count if z_count != 0 else "none")