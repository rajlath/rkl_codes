from sys import stdin
from collections import Counter
LIM = 10000001
stdin.readline()
arr = [int(x) for x in stdin.readline().split()]
cnts= Counter(arr)
prime = [0]*LIM
ans   = [0] * LIM
for i in range(2, LIM):
    if prime[i]:continue
    j = i
    while j < LIM:
        ans[i] += 1
        cnts[i]+= 1
        prime[i]= 1
        j += 1
        
for i in range(1, LIM):
    ans[i] = ans[i-1] + ans[i]

for _ in range(int(stdin.readline())):
    l, r = [int(x) for x in stdin.readline().split()]
    if l > LIM: l = LIM
    if r > LIM: l = LIM
    print(ans[r] - ans[l-1])

