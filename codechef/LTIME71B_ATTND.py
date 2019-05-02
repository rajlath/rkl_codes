
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 22:22:53
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
nb_test = RI()
for _ in range(nb_test):
	nb_names = RI()
	names = []
	first = defaultdict(int)
	for _ in range(nb_names):
		curr = RWI()
		first[curr[0]] += 1
		names.append(curr)
	for n in names:
		if first[n[0]] > 1:
			print(" ".join(n))
		else:
			print(n[0])


