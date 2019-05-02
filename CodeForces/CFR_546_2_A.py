
# -*- coding: utf-8 -*-
# @Date    : 2019-03-11 22:17:37
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


nb_chapters = RI()
done = 0
pages = {}
for _ in range(nb_chapters):
    s, e = RMI()
    for i in range(s, e+1):
        pages[i] = pages.get(i, 0) + done
    done += 1
#print(pages)
curr = int(input())
print(nb_chapters - pages[curr])

