'''
3
4
13 6 12 19
25
5
4 1 16 15 2
17
8
1 16 2 15 4 12 22 7
0
'''
from collections import defaultdict
for _ in range(int(input())):
    nos = int(input())
    arr = [int(x) for x in input().split()]
    tgt = int(input())
    match = defaultdict(int)
    found = False
    for i,v in enumerate(arr):
        if v in match and tgt-v != v:
            print(match[v], i)
            found = True
            break
        else:
            match[tgt-v] = i
    if not found:print(-1, -1)
