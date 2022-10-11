# Could use some improvement, will clean in repository
# Typing a two or one digit number doesnt return a warning, work on this
# Try to integrate continous typing

def reverse(rev, number):
    if number < 1000 and number > 99:
        while number > 0:
            rev = rev * 10 + (number % 10)
            number = number // 10
        if rev == 0:
            print("Enter Three Digits only!")
        else:
            print(rev)

try:
    rev = 0
    number = int(input("Enter a Three Digit number: "))


    reverse(rev, number)
except:
    print("Please enter Numerical values only!")
