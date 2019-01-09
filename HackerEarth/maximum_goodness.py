
# -*- coding: utf-8 -*-
# @Date    : 2018-10-28 22:15:28
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

from collections import defaultdict

lens = read_int()
arrs = read_ints()
arr1 = [1 if x == 1 else -1 for x in arrs ]
max_so_far = min_val
max_end_here=0
start = 0
end   = 0
s = 0
for i in range(lens):
    max_end_here += arr1[i]
    if max_so_far < max_end_here:
        max_so_far = max_end_here
        start = s
        end   = i
    if max_end_here < 0:
        max_end_here = 0
        s = i + 1
print(end - start + 1)