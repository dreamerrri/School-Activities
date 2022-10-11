def test():
    try:
        num = int(input("Enter how many input to be accepted: "))
        pack = []

        for i in range(num):
            pack.append(int(input("Enter a Number: ")))
        x = min(pack)
        y = max(pack)

        print(" ")
        print("Largest: ", y)
        print("Smallest: ", x)
    except:
        print("Please enter only Digits!")
        test()


test()
