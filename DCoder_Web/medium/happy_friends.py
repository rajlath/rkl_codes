for _ in range(int(input())):
    lens = int(input())
    vals = sorted([int(x) for x in input().split()])
    k = int(input())
    print(sum(vals[:k]))
