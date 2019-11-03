for _ in range(int(input())):
    c, m , x = [int(x) for x in input().split()]
    can_do = min(c, m)
    sums = sum([c, m, x])
    if sums >= can_do * 3:
        print(can_do)
    else:
        print(sums // 3)
