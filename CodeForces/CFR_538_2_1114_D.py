'''
from itertools import groupby
import operator
lens = int(input())
squares = [int(x) for x in input().split()]
sqg = groupby(squares)
dicts = {}
for k, g in sqg:
    dicts[k] = dicts.get(k, 0) + 1
max_key = ''
max_con = 0
for k, v in dicts.items():
    #print(k, v)
    if v > max_con:
        max_key = k
        max_con = v
ans = 0
for k, _ in groupby(squares):
    if k != max_key:
        ans += 1
print(ans)
'''
n=int(raw_input())
lsr = map(int, raw_input().split())
ls = [lsr[0]]
for le in lsr[1:]:
if le!=ls[-1]:
        ls.append(le)

n=len(ls)
dpa=[]
dpb=[0 for i in range(n+1)]
for sz in range(2,n+1):
dp=[]
for start in range(n-sz+1):
        if ls[start] == ls[start+sz-1]:
        dp.append(min(dpb[start], dpb[start+1], dpa[start+1])+1)
        else:
        dp.append(min(dpb[start], dpb[start+1])+1)
dpa, dpb = dpb, dp
print dpb[0]





