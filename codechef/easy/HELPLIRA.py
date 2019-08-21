
# -*- coding: utf-8 -*-
# @Date    : 2019-07-21 12:59:36
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
nb_triangle = int(input())
mins = 0
maxs = 0
ax, ay, bx, by, cx, cy = [int(x) for x in input().split()]
area = abs((ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) / 2)
'''
areas = []
for _ in range(int(input())):
    ax, ay, bx, by, cx, cy = [int(x) for x in input().split()]
    area = abs((ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) // 2)
    areas.append(area)
print(areas.index(min(areas)) + 1, areas.index(max(areas)) + 1)
