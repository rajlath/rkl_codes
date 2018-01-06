for _ in range(int(input()):
    counts = int(input())
    boys   = [int(x) for x in input().split()]
    girls  = [int(x) for x in input().split()]
    bb, gg = {}, {}
    for i in range(counts):
        if boys[girls[i]] != i:
            t = boys[girsl[i]]
            gg[t] = gg.get(t, 0) + 1
        if girls[boys[i]] != i:
            t = girls[boys[i]]
            bb[t] = bb.get(t, 0) + 1
       


