# Python program that will ask for a starting number and ending number.
# The program will count the Even numbers and the Odd numbers from the inputted starting value to the inputted ending value.
# Displays the count of even and odd numbers.
# Displays the sum of all even numbers.
# Displays the sum of all odd numbers.

num1 = int(input("Enter a starting number: "))
num2 = int(input("Enter an ending number: "))
even = 0
odd = 0
evensum = 0
oddsum = 0

for num in range(num1, num2+1):
    if(num%2 == 0):
        even = even + 1
        evensum = evensum + num
    else:
        odd = odd + 1
        oddsum = oddsum + num

print(" ")
print("Count of Even numbers: ", even)
print("Sum of all Even numbers: ", evensum)
print("Count of all Odd numbers: ", odd)
print("Sum of all Odd numbers: ", oddsum)
