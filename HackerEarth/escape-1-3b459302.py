
# -*- coding: utf-8 -*-
# @Date    : 2018-10-06 10:57:53
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

distance, speedM, speedT = read_ints()
if distance == 0:
    ans = 0
elif speedM <= speedT:
    ans = -1
else:
    time_to_catch = (distance / (speedM - speedT))
    ans = 2 * time_to_catch
print('{0:.6f}'.format(ans))

