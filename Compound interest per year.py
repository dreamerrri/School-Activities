# A python program that will ask for amount of investment, number of years, and interest rate.
# Then coomputes for the accumulated total invest for every year and display result.
# This shit is the whole reason I made this github page, In hopes I could help my fellow students out.

inv = float(input("Enter Amount of Investment: "))
year = int(input("Enter how many Years: "))
rate = float(input("Interest Rate: "))
i = 0
count = 0

print(" ")
for i in range(1, year+1):
        accinv = inv * (1 + rate / 100) ** i
        print("Accumulated Investment in Year",(count+1),": {:.1f}".format(accinv))
        count = count + 1
