
# -*- coding: utf-8 -*-
# @Date    : 2019-01-30 20:41:28
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


nb_landings, interval = read_ints()
prev_landing = 0
for _ in range(nb_landings):
    hour, minute = read_ints()
    last_landing = hour * 60 + minute
    if last_landing  - prev_landing <= interval:
        prev_landing = last_landing + interval + 1
    else:break
print(prev_landing //  60, prev_landing % 60)


