
# -*- coding: utf-8 -*-
# @Date    : 2018-09-21 20:07:28
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
def divisible_by_3(n)  : return sum([int(x) for x in str(n)]) % 3 == 0


n = read_int()

#solution 1 @eugalt
if n%3 == 2:print(2, 2, n-4)
else:print(1, 1, n-2)

'''
#solution 2 ecnerwala
x = n%3or 1
print(1, x, n-x-1)

#solution 3 neal
x = n%3>1
print(1, x+1, n-2-x)
'''












