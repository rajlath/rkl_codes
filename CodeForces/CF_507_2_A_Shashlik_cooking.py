
# -*- coding: utf-8 -*-
#! @Date    : 2018-09-06 07:53:13
#! @Author  : raj lath (oorja.halt@gmail.com)
#! @Link    : "http://codeforces.com/contest/1040/problem/B"
#! @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline()]
def read_str_list(): return [x for x in stdin.readline().split()]

nops, k = read_ints()
OFFSET = 2 * k + 1
rem  = nops % OFFSET
if nops < k+1:ans = [1]
elif rem <= k and rem != 0:
    ans = range(k + 1 - (k + 1-rem), nops+1, OFFSET)
else:
    ans = range(k + 1, nops + 1, OFFSET)
print(len(ans))
print(*ans)




