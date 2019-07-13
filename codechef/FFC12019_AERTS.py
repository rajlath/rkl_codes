
# -*- coding: utf-8 -*-
# @Date    : 2019-06-21 13:02:40
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
from collections import defaultdict

def dfs(n):
    global visited, adjs, stks
    visited[n] = True
    for i in range(len((adjs[n]))):
        cur = adjs[n][i]
        if not visited[cur]: dfs(cur)
    stks.append(n)

n, m  = RMI()
arrs  = RMI()
adjs  = defaultdict(list)
sadj  = defaultdict(list)
visited = [False] * n
stks  = []
v = []
for i in range(m):
    x, y = RMI()
    adjs[x].append(y)
    sadj[y].append(x)
for i in range(n):
    if not visited[i]:
        dfs[i]
visited = []
while stks:
    cur = stks[0]
    stks.pop(0)
    if visited[cur]:continue
     sums = 0
     dfs1(cur)






