def valid(n):
    for i in ["0", "4", "8"]:
        if i in n:
            return i
    has = False
    for i in ["2", "6"]:
        if i in n:
            indx = n.rfind(i)
            has = True
            return int(n[indx] + i )
    return -1

nb_test = int(input())
for _ in range(nb_test):
    ins = input()
    res = valid(ins)
    if res == -1:
        print("NO")
    else:
        print("YES", res)



