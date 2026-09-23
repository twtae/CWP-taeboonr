#!/usr/bin/python3

array = [1, 2, 6, 7, 67, 76, 2, 1]
new_array = [i + 2 for i in array if i > 5]

print(f"Original array: {array}")
print(f"New array: {new_array}")