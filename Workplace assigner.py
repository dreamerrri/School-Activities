# A Python program that will ask user to enter age, sex ( M or F ), then prints their workplace.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere.
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# Any other input of age should print "ERROR"

Age = int(input("Enter age: "))
Sex = input("Enter Sex(or F): ")

if Sex == "M" or "m" and Age <= 40:
    print("You may work anywhere.")
elif Sex == "M" or "m" and Age <= 60:
    print("You may only work in Urban Areas.")
elif Age >= 90:
    print("ERROR")
else:
    print("You may only work in Urban Areas.")
