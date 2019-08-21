for _ in range(int(input())):
    stops = int(input())
    vals  = [int(x) for x in input().split()]
    maxs, pos = 0, -1
    for i in range(stops):
        if maxs + pos <= vals[i] + i:
            maxs = vals[i]
            pos  = i
    print(maxs + pos)        
