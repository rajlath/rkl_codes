'''
Examples
inputCopy
3
1 2
7 2
3 10
4
1 4
2 4
3 4
4 4
outputCopy
24
inputCopy
1
1000000000 239
3
14 15
92 65
35 89
outputCopy
408
'''
from collections import defaultdict
costs = defaultdict(list)
nos_cf = int(input())
for i in range(nos_cf):
    i, c = [int(x) for x in input().split()]
    costs[i].append(c)
nos_tf  = int(input())
for i in range(nos_tf):
    i, c =  [int(x) for x in input().split()]
    costs[i].append(c)
ans = 0
for i, v in costs.items():
    ans += max(v)
print(ans)

