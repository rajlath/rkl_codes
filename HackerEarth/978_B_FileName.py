
'''
Examples
inputCopy
6
xxxiii
outputCopy
1
inputCopy
5
xxoxx
outputCopy
0
inputCopy
10
xxxxxxxxxx
outputCopy
8
'''
from itertools import groupby
noe = int(input())
arr = input()
arrg = groupby(arr)
cnt = 0
for i, v in arrg:
    curr = "".join(v)
    currs=list(set(curr))
    if len(currs) == 1 and currs[0] == "x":
        cnt += (max(0, len(curr) - 2))
print(cnt)
