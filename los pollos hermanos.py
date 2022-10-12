def menu():
    price1 = int(999)
    price2 = int(759)
    price3 = int(699)
    price4 = int(429)
    price5 = int(259)
    price6 = int(99)
    price7 = int(99)

    h = int(99)
    i = int(99)
    j = int(99)
    k = int(99)
    l = int(99)
    m = int(99)
    n = int(99)

    print(" ")
    print("Los Pollos Specials\t\t\t\t\t\t\tPrice\t\t\t\tQuantity")
    print(" ")
    print("[1] Whole Chicken Menu", "                     ", price1, "                 ", h)
    print("[2] Huevos Rancheros", "                       ", price2, "                 ", i)
    print("[3] Green White Stew", "                       ", price3, "                 ", j)
    print("[4] Pollos Chicken Breakfast", "               ", price4, "                 ", k)
    print("[5] Hermanos Burger", "                        ", price5, "                 ", l)
    print("[6] Curly Fries", "                             ", price6, "                 ", m)
    print("[7] Pollos Soda", "                             ", price7, "                 ", n)
    print("[0] Take Order")


menu()
option = int(input("Enter your Option: "))

while option != 0:
    if option == 1:
        print("Picked Menu 1")
    elif option == 2:
        amount = int(input("Enter Amount: "))
        print("Picked Menu 2")
    elif option == 3:
        amount = int(input("Enter Amount: "))
        print("Picked Menu 3")
    elif option == 4:
        amount = int(input("Enter Amount: "))
        print("Picked Menu 4")
    elif option == 5:
        amount = int(input("Enter Amount: "))
        print("Picked Menu 5")
    elif option == 6:
        amount = int(input("Enter Amount: "))
        print("Picked Menu 6")
    elif option == 7:
        amount = int(input("Enter Amount: "))
        print("Picked Menu 7")
    else:
        print("Invalid Option")
    print()
    menu()
    option = int(input("Enter option: "))

print("thanks")
