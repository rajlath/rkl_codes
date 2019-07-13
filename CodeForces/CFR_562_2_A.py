
# -*- coding: utf-8 -*-
# @Date    : 2019-05-26 21:23:56
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
s="NO"
n, a, x, b, y=map(int, input().split())
i=1
while a!=x and b!=y:
    a+=1
    b-=1
    if a>n:
        a=1
    if b<1:
        b=n
    if a==b:
        s="YES"
        break
print(s)


nb_st, sta, ena, stb, enb = RMI()
ans = "NO"
a, b = sta, stb
while a != ena and b != enb:
    a += 1
    if a > nb_st: a = 1
    b -= 1
    if b < 0: b = nb_st

    if a == b:
        ans = "YES"
        break
print(ans)

routeA = []
i = sta
while True:
    routeA.append(i)
    if i == ena:break
    i += 1
    if i == nb_st + 1:i = 1
routeB = []
i = stb
while True:
    routeB.append(i)
    if i == enb:break
    i -= 1
    if i == 0:
        i = nb_st
#print(routeA, routeB)

ans = "NO"
for x, y in zip(routeA, routeB):
    print(x, y)
    if x == y:
        ans = "YES"
        break
print(ans)
'''

ans = "NO"
n, a, x, b, y=RMI()
while(a != x and b != y):
    a += 1
    b -= 1
    if a > n : a = 1
    if b < 1 : b = n
    if a == b:
        ans = "YES"
        break
print(ans)


