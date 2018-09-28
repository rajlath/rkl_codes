
# -*- coding: utf-8 -*-
# @Date    : 2018-09-22 15:46:14
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.hackerrank.com/contests/recode-2/challenges/humpty-dumpty
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_test = read_int()
for _ in range(nb_test):
    lens = read_int()
    line = read_str()
    stack = []
    cnt   = 0
    for i in line:
        if len(stack)==0 or stack[-1] == i:
            stack.append(i)
        else:
            cnt += 1
            stack.pop()
    print(("Humpty Dumpty", "King")[cnt%2==0])


