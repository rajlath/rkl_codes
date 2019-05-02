

# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 14:57:31
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



nb_test = RI()
for _ in range(nb_test):
    cols = RI()
    encrypted = RW()
    rows = len(encrypted) // cols
    grid = []
    i = 0
    while i < (len(encrypted)):
        curr = encrypted[i:i + cols]
        grid.append([x for x in curr])
        i += cols
    traversed = list(zip(*grid))
    decrypted = ''
    for i in traversed:
        decrypted += ''.join(i)
    print(decrypted)