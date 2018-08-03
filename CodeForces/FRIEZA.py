for _ in range(int(input())):
    s = input()
    R = ""
    i = 0
    while i < len(s):

        if s[i] in "frieza":
            c = 0
            while s[i] in "frieza":
                c += 1
                i += 1
            R += str(c)

        else:
            c = 0
            x = 1
            while s[i] not in "frieza":
                c += 1
                i += 1
                print(x)
                x += 1

            R += str(c)
            

    print(R)







