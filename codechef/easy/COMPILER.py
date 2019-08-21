for _ in range(int(input())):
    expr = input()
    stck = []
    count = 0
    for indx, i in enumerate(expr):
        if i == ">":
            if len(stck) == 0:
                break
            else:
                stck.pop()
                if len(stck) == 0:
                    count = indx + 1
        else:
            stck.append(i)
    print(count)
