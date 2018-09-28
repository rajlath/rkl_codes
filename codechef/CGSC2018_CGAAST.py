
# -*- coding: utf-8 -*-
# @Date    : 2018-09-24 09:24:59
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    :
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

'''
Sample Input:
3
army
mary
curse
cease
stressed
desserts

Sample Output:
Arjun
Amit
Arjun
'''
nb_test = read_int()
for _ in range(nb_test):
    s1 = read_str()
    s2 = read_str()
    if sorted(s1) == sorted(s2):
        print("Arjun")
    else:
        print("Amit")

