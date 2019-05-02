
# -*- coding: utf-8 -*-
# @Date    : 2019-03-16 11:34:31
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from collections import defaultdict
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

def DFS(ii):
    global done
    done[ii] = True
    for i in range(len(hiearchy[i])):
        if not done[hiearchy[ii][i]]:
            DFS(hiearchy[ii][i])
            income = hiearchy[ii][i]
            x      = 

nb_people, *others = RMI()
earning = others[:nb_people]
ids     = others[nb_people:]
hiearchy= defaultdict(list)
for i in range(nb_people):
    hiearchy[ids[i] - 1].append(i)
hojo = hiearchy[-2][0]
done = [False] * nb_people
max_value = earning[hojo]
min_value = 0

def DFS(i):
    global done, max_value, min_value
    done[i] = True
    if not hiearchy[i]:return min_value
    else:
        p = []
        for i1 in hiearchy[i]:
            if not done[i1]:
                min_value  = max(min_value, max_value - earning[i1])
                max_value  = max(max_value, earning[i1])
                ids.append(DFS(i1))
        return max(ids)

print(DFS(hojo))





