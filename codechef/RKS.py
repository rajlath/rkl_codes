
# -*- coding: utf-8 -*-
# @Date    : 2019-01-27 12:22:09
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


nb_Test = int(input())
for _ in range(nb_Test):
    n, k = read_ints()
    r = set(range(1, n+1 ))
    c = set(range(1, n+ 1))
    for i in range(k):
        r1, c1 = read_ints()
        r.remove(r1)
        c.remove(c1)
    print(len(r), end= " ")
    for i in range(len(r)):
        r1 = r.pop()
        c1 = c.pop()
        print(r1, c1, end=" ")



