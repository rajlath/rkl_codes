
# -*- coding: utf-8 -*-
# @Date    : 2018-10-21 18:32:13
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

#learned from solution by  knchef59

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

limit = 1000001
mods  = 1000000007

pf_count = [0] * limit
primes   = [1] * limit

for i in range(2, limit):
    if primes[i]:
        pf_count[i] += i
        j = i * 2
        while j < limit:
            pf_count[j] += i
            primes[j] = 0
            j += i
nb_test = read_int()
for _ in range(nb_test):
    left, rite = read_ints()
    print(sum(pf_count[left:rite+1]) % mods)



