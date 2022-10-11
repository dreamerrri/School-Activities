def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def quotient(a, b):
    return a / b

def test():
    try:
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))

        w = add(num1, num2)
        print("The Sum is: ",w)

        x = subtract(num1, num2)
        print("The Difference is: ",x)

        y = multiply(num1, num2)
        print("The Product is: ",y)

        z = quotient(num1, num2)
        print("The Quotient is: ",z)

    except:
        print("Please enter a Number only!")
        print(" ")
        test()


test()
