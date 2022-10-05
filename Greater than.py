# A simple program that decides which of the inputted values are greater.

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

if num1 > num2:
    print("The Greater Value is:", num1)
elif num1 < num2:
    print("The Greater Value is:", num2)
else:
    print("The Two inputted Numbers are equal")
