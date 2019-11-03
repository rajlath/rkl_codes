for _ in range(int(input())):
    nbs = int(input())
    val = [0, 0]
    can = False
    for q in range(nbs):
        m, a, b = [int(x) for x in input().split()]
        if m == 1 or a == b:
            can = True
            print("YES")
            val[0], val[1] = a, b
        elif m == 2:
            if can == False:
                print("NO")
            elif a < max(val) or b < max(val)        :
                print("YES")
                val[0], val[1] = a, b
            else:
                print("NO")


