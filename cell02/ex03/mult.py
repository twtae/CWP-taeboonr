#!/usr/bin/python3

a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))

mul = a * b

print(f"{a} x {b} = {mul}")

if mul < 0:
    print("The result is negative.")
elif mul > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")