# A Python program that will ask a number input from the user, then determine whether the inputted number is a ODD number or EVEN.

input = int(input("Enter a number: "))

X = input % 2

print(" ")
if X == 0:
  print("EVEN")
else:
  print("ODD")
