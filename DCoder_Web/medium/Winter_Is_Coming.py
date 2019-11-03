for _ in range(int(input())):
    lens = int(input())
    vals = [int(x) for x in input().split()]
    maxs = [0, 0]
    for i, v in enumerate(vals):
        maxs[i%2] += v
    print(max(maxs))