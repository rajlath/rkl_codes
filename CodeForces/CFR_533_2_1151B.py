
# -*- coding: utf-8 -*-
# @Date    : 2019-04-19 15:30:49
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

rows, cols = RMI()
matrix = [ RMI() for _ in range(rows)]
ans = [0] * rows
xor = 0
for i in range(rows):
    xor ^= matrix[i][0]
for i in range(rows):
    if xor > 0:
        break
    for j in range(cols):
        curr = xor ^ matrix[i][0] ^ matrix[i][j]
        if curr > 0:
            ans[i] = j
            xor = curr
            break
if xor == 0: print("NIE")
else:
    print('TAK')
    print(*map(lambda x: x + 1, ans))
