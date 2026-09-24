#!/usr/bin/python3

import sys

def shrink(text: str):
    print(text[:8])

def enlarge(text: str):
    print(text + ('Z' * (8 - len(text))))

if len(sys.argv) == 1:
    print("none")
else:
    for text in sys.argv[1:]:
        shrink(text) if len(text) > 8 else enlarge(text)