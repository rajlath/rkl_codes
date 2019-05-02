
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 15:37:29
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


#! Solution by xumouyi

def solve(p, q, r):
    ans = ""
    current = r
    i = p
    j = q
    while True:
        if j < i:
            break
        if current < num[i] < num[j] or num[j] <= current < num[i]:
            ans += "L"
            current = num[i]
            i += 1
            continue
        if current < num[j] < num[i] or num[i] <= current < num[j]:
            ans += "R"
            current = num[j]
            j -= 1
            continue
        if current < num[i] == num[j]:
            ans1 = solve(i, j - 1, num[i])
            ans2 = solve(i + 1, j, num[i])
            if len(ans1) > len(ans2):
                ans += "R" + ans1
            else:
                ans += "L" + ans2
        break
    return ans

n = int(input())
num = [*map(int, input().split())]
ans = solve(0, n - 1, -1)
print(len(ans))
print(ans)