#!/usr/bin/python3

num = input("Give me a number: ").strip()
try:
    num = float(num)
    if (num.is_integer()):
        raise Exception()
    else:
        print("This number is a decimal.")
except:
    print("This number is an integer.")