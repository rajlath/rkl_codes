
# -*- coding: utf-8 -*-
# @Date    : 2019-03-05 13:00:03
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

def valids(a, b):
    if a[0] <= b[0] and a[1] <= b[1]:return False
    a[0], a[1] = a[1], a[0]
    if a[0] <= b[0] and a[1] <= b[1]:return False
    return True

nb_Test = RI()
pairs = [(0, 0)] * nb_Test
widths = [int(x) for x in input().split()]
height = [int(x) for x in input().split()]
for i in range(nb_Test):
    if pairs[i][0] < pairs[i][1]:
        pairs[i][0],pairs[i][1] = pairs[i][1], pairs[i][0]
sorted(pairs)
dp = [0 for x in range(nb_Test + 5)]
ans = 1
for i in range(nb_Test - 1, -1, -1):
    dp[i] = 1
    j = nb_Test - 1
    while j >= i:
        if valids(pairs[i], pairs[j]):
            dp[i] = max(dp[j] + 1, dp[i])
        j -= 1
    ans = max(ans, dp[i])
print(ans)

