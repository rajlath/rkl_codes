nb = int(input())
for _ in range(nb):
    N, Q = [int(x) for x in input().split()]
    powers = [int(x) for x in input().split()]
    counts = [0] * (N + 1)
    for _ in range(Q):
        x, y = [int(x) for x in input().split()]
        for i in range(x-1, y):
            counts[i] += 1
    maxs = 0
    #print(counts)
    for i in range(N - 1, -1, -1):
        if maxs <= counts[i]:
            maxs = counts[i]
            anss = powers[i]
    print(anss)



