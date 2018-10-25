
# -*- coding: utf-8 -*-
# @Date    : 2018-10-13 15:57:03
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
from itertools import accumulate
import bisect
nb_test = read_int()
for _ in range(nb_test):
    nb_student, nb_books = read_ints()
    pages = read_ints()
    left = read_ints()
    rite = read_ints()

    pages.sort()
    pre_sum = [0] + list(accumulate(pages))
    for i in range(nb_books):
        lft = bisect.bisect_left(pages, left[i])
        rit = bisect.bisect_right(pages , rite[i]) - 1
        print(lft, rit)
        if rit < lft: print(0, 0)
        elif lft == rit:print(1, pages[lft])
        else:print(rit - lft -1, pre_sum[rit + 1] - pre_sum[lft])





