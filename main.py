h = int(10)
i = 0
space = 1
space2 = 0
while i < h:
    for i in range(1,h+1):
        ha = 1 * i
        d = 7 * i
        space2 = space2 + 1
        if space == space2:
            print("Human Age(1-10 years Old)","   ", "Dog Age")
        print("         ", ha,"                   ", d)