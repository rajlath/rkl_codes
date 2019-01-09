
# -*- coding: utf-8 -*-
# @Date    : 2018-11-24 08:40:37
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
from math import ceil, floor
sheets = {"R":2, "G":5, "B":8}
nb_student, per_sheet = read_ints()
ans = 0
for c in ["R", "G", "B"]:
    needed = (nb_student * sheets[c])
    curr =   int(needed / per_sheet)
    curr +=  ((needed % per_sheet) > 0)
    ans += curr
print(ans)





