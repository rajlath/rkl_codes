for _ in range(int(input())):
    s = list(input())
    uc = []
    lc = []
    for i in s:

        if i.isupper():
            uc.append(i)
        else:
            lc.append(i)

    print(''.join(uc+lc))