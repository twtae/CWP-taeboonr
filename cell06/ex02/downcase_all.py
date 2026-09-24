#!/usr/bin/python3

import sys

def downcase_all(params: list[str]):
    if len(params) == 0:
        print("none")
    else:
        for param in params:
            print(param.lower())

downcase_all(sys.argv[1:])