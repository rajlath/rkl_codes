from collections import Counter
lens = int(input())
vals = Counter([int(x) for x in input().split()])
noq = int(input())
for _ in range(noq):
    curr = int(input())
    if curr in vals:
        print(vals[curr])
    else:
        print(-1)