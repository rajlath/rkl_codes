'''
1
10 2
30 31 32 33 32 32 31 30 30 32
1
3
'''
from collections import Counter
for _ in range(int(input())):
    nbs, nq = [int(x) for x in input().split()]
    sizes   = Counter([int(x) for x in input().split()])
    size    = []
    for i, v in sizes.items():
        size.append([v, i])
    sizes = sorted(size, reverse=True)
    for i in range(nq):
        k = int(input())
        ans = 0
        for i in range(k):
            ans += sizes[i][0]
        print(ans)




