
# -*- coding: utf-8 -*-
# @Date    : 2019-02-28 15:47:00
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
RMI1 = lambda : [int(x) - 1 for x in sys.stdin.readline().strip().split()]


nb = RI()
s1, s2 = RMI1()
e1, e2 = RMI1()

m = []

for _ in range(nb):
    m.append(RWI())

uni = [[] for _ in range(2)]

s = 0
moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(x, y):
    q = [[x, y]]
    while len(q):
        i, j = q.pop()
        m[i][j] = "1"
        uni[s].append([i, j])
        for a, b in moves:
            ni = i + a
            nj = j + b
            if ni >=0 and nj >= 0 and ni < n and nj < n:
                if m[ni][nj] == "0":
                    q.append([ni, nj])

bfs(s1, s2)
if m[e1][e2] == 1:
    print(0)
else:
    s += 1
    bfs(e1, e2)
    


