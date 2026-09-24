#!/usr/bin/python3

def add_one(num: int):
    num += 1

num = 67
print(f"before: {num}")
add_one(num)
print(f"after: {num}") # Same as before