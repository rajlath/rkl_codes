
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 10:09:45
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


from sys import stdin
input = stdin.readline

n, k = (int(x) for x in input().split())
s = input()[:-1]
if k - 1 <= n - k:
    print('LEFT\n' * (k - 1), end='')
    print('PRINT', s[0])
    for c in s[1::]:
        print('RIGHT')
        print('PRINT', c)
else:
    print('RIGHT\n' * (n - k), end='')
    print('PRINT', s[-1])
    for c in s[-2::-1]:
        print('LEFT')
        print('PRINT', c)