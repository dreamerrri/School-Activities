# A program that displays the sum of two inputted variable.
# Then asks the user if they want to stop the operation.
# The operand(+) is interchangeable with any operations.
# Could use some improvement as typing a numerical value in Y/N questions still runs the task.

yn = "Y"
while yn != "N":
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    sum = num1 + num2
    print("The Sum of", num1, "and", num2, "is", sum)
    print(" ")
    yn = input("Do you want to continue(Y/N)?: ")
    print(" ")
else:
    print("Thank You")
