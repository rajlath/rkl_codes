
# -*- coding: utf-8 -*-
# @Date    : 2019-05-18 08:46:40
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0


#thanks to tau_ram_ram
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

first_letter = defaultdict(int)
nb_names = RI()
pairs = 0
for _ in range(nb_names):
  first_letter[RW()[0]] += 1
for letter in first_letter:
  curr = first_letter[letter]
  pair = curr // 2
  nons = curr - pair
  pairs += (pair * (pair - 1)) // 2
  pairs += (nons * (nons - 1)) // 2
print(pairs)

