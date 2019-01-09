
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 14:31:28
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

lens = read_int()
best = [0] * lens
elem = read_ints()
selem= sorted(elem)
for i in range(lens):
    current = 0
    for j in range(i):
        if selem[i] % selem[j] == 0 and current < best[j]:
            current = best[j]
    best[i] = current + 1
print(max(best))

