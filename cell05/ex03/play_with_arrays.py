#!/usr/bin/python3

array = [1, 2, 6, 7, 67, 67, 2, 1]
new_set = {i + 2 for i in array if i > 5}

print(array)
print(new_set)