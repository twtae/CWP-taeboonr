#!/usr/bin/python3

a = int(input("Give me the first number: "))
b = int(input("Give me the second number: "))

print("Thank you!")

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} / {b} = {a / b:g}" if b != 0 else "Cannot divided by 0")
print(f"{a} * {b} = {a * b}")