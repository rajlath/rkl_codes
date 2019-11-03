for _ in range(int(input())):
    lens = int(input())
    vals = sorted([int(x) for x in input().split()])
    anss = vals[0] % vals[1]
    for i in vals[2:]:
        anss %= i
    print(anss)