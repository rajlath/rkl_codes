
# -*- coding: utf-8 -*-
# @Date    : 2019-08-26 19:38:59
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

'''
for _ in range(RI()):
    curr = RI()
    counts = 0
    for i in range(1, curr):
        for j in range(1, curr):
            for k in range(1, curr):
                if i + j + k == curr:
                    if [i, j, k].count(max([i, j, k])) == 1:
                        counts += 1
    print(counts)
'''
dp = [[[-1 for i in range(4)] for i in range(501)] for i in range(501)]

def countWaysUtil(n, parts, next_part):
    if n <= 0:return 0
    if dp[n][next_part][parts]  != -1:return  dp[n][next_part][parts]
    ans = 0
    for i in range(next_part, n + 1):
        ans += countWaysUtil(n - i, parts - 1, i)
    dp[n][next_part][parts] = ans
    return ans

print(countWaysUtil(5, 3, 1))
