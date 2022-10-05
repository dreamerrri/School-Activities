# A python program that will compute for the human age(1-10 years old) equivalent to the age of dogs.
# I still do not know how to seperate outputs like a table, so pardon the heinous spaces, it would help if somebody teaches me how.

h = int(10)
i = 0
space = 1
space2 = 0

while i < h:
    for i in range(1, h+1):
        ha = 1 * i
        d = 7 * i
        space2 = space2 + 1
        if space == space2:
            print("Human Age(1 - 10 Years)","  ","Dog Age")
        print("        ", ha,"                  ", d)
        #please teach me how
