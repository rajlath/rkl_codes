
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

from collections import Counter
nb_flower  = read_int()
flowers    = Counter(read_ints())
maxf, minf = max(flowers), min(flowers)
res1 = maxf - minf
res2 = flowers[maxf] * flowers[minf] if res1 else flowers[maxf]*(flowers[maxf]-1)//2
print(res1, res2)