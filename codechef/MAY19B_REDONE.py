
# -*- coding: utf-8 -*-
# @Date    : 2019-05-18 12:55:32
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


def prebuild_valids():
  mods = pow(10, 9) + 7
  done = 1
  valids = [0]
  while done < 1000000:
    current = (done + valids[done - 1] + done * valids[done - 1]) % mods
    valids.append(current)
    done += 1
  return valids

valid = prebuild_valids()
nb_test = RI()
for _ in range(nb_test):
  print(valid[RI()])

