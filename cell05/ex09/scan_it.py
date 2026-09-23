#!/usr/bin/python3

import re
import sys

if (len(sys.argv) != 3):
    print("none")
else:
    substr_list = re.findall(sys.argv[1], sys.argv[2])
    print("none" if len(substr_list) == 0 else len(substr_list))