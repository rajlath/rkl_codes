from operator import mul
from functools import reduce
maxs = 1000010
a = [0]*maxs
s = [[[x for x in range(10)] for y in range(maxs)]]

for i in range(1, maxs):
    if i < 10:
        a[i] = i
    else:
        x, m = i, 1
        while x:
            if x%10>0: m*= x%10
            x//=10
        a[i] = m
    for j in range(1,10):
        s[i][j] = s[i-1][j] + (a[i] == j)
for _ in range(int(input())):
    l, r, k = [int(x) for x in input().split()]
    print(s[r][k] - s[l-1][k])







