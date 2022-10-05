# Celsius to Fahrenheit converter and vice versa.
# Could use an improvement.
# Need to figure out how to use multiple range if conditions.

fa = float(input("Fahrenheit: "))
ce = float(input("Celsius: "))

f2c = 5 / 9 * (fa - 32)
c2f = (9 / 5) * ce + 32

print(" ")
if 22 < f2c < 32 and 71.6 < c2f < 89.6:
    print(fa, "degrees fahrenheit is equal to: {:.2f}".format(f2c), "degrees Celsius. Warm and good weather today!")
    print(ce, "degrees celsius is equal to: {:.2f}".format(c2f), "degrees Fahrenheit. Warm and good weather today!")
elif 71.6 < f2c < 89.6 or 71.6 > c2f > 89.6:
    print(fa, "degrees fahrenheit is equal to: {:.2f}".format(f2c), "degrees Celsius. Warm and good weather today!")
    print(ce, "degrees celsius is equal to: {:.2f}".format(c2f), "degrees Fahrenheit. Let us not go outside!")
elif 71.6 > f2c > 89.6 or 71.6 < c2f < 89.6:
    print(fa, "degrees fahrenheit is equal to: {:.2f}".format(f2c), "degrees Celsius. Let us not go outside!")
    print(ce, "degrees celsius is equal to: {:.2f}".format(c2f), "degrees Fahrenheit. Warm and good weather today!")
else:
    print("invalid")
