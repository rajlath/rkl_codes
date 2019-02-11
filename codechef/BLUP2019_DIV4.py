nb_Test = int(input())
for _ in range(nb_Test):
    inss = list(input())
    if inss[-1] == "4":
        print("YES",4)
    elif inss[-1] == "0":
        print("YES" , 0)
    else:
        last = int(inss.pop())
        i = 1
        while inss:
            curr = int(inss.pop())
            i += 1
            if (curr + last)%4==0:
                print("".join(inss[:-i]))
        if i == len(inss):
            print("NO")




