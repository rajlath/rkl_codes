for _ in range(int(input())):
    lens = int(input())
    vals = [int(x) for x in input().split()]
    vals = [x for x in vals if x <= 2048]
    if sum(vals) < 2048:
        print("NO")

    else:
        print("YES")