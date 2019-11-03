'''
3
7
5 2 5 7 2 9 7
5
7 2 3 7 2
6
3 4 0 3 0 4
'''
from collections import Counter
for _ in range(int(input())):
    nbs = int(input())
    cnt = Counter([int(x) for x in input().split()])
    ans = -1
    for i, v in cnt.items():
        if v == 1:
            ans = i
            break
    print(ans)

