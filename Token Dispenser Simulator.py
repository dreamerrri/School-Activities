# A program that emulates a Token Dispenser.
# This was horrible, but a worth it experience nonetheless.

token = int(input("Enter token stocks: "))
dispense = int(input("How many do you wish to dispense?: "))

print(" ")
if token >= dispense:
    for i in range(0, dispense):
        print("token")
elif token < dispense:
    for i in range(0, token):
        print("token")
    print("Exceeded amount of Tokens")
