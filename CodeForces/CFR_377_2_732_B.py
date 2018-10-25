
# -*- coding: utf-8 -*-
# @Date    : 2018-10-02 08:00:37
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
'''
nb_peoples = read_int()
times = []
for _ in range(nb_peoples):
    h, m = read_ints()
    times.append(h*60 + m)
stack = [times[0]]
cash  = 1
for i in times[1:]:
    cash += i == stack[-1]
    stack.append(i)
print(cash)
'''

nb_days, min_walk = read_ints()
walks = read_ints()
valid = [0] * nb_days
valid[0] = walks[0]
for i in range(1, nb_days):
    valid[i] = max(walks[i], min_walk - valid[i-1])
print(sum(valid) - sum(walks))
print(*valid)
