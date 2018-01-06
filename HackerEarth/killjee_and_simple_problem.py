'''
3
1 2 1
'''
from math import pow
noe = int(input())
arr = [int(x) for x in input().split()]
sums = [0] * (noe + 1)
for i in range(noe):
    sums[i+1] = sums[i] + arr[i]
s = set()
for i in range(1, noe+1):
    for j in range(i,noe+1 ):
        s.add(sums[j] - sums[i-1])
print(len(s))


