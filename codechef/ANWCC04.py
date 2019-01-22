
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 19:44:53
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

import re
nb_Test = int(input())
for _ in range(nb_Test):
    ins = input()
    numbers = [int(x) for x in re.findall(r'\d+', ins)]
    ops     = [x for x in ins if x in ["+", "-"]]
    ans = numbers[0]
    for i in range(2):
        if ops[i] == "+":
            ans += numbers[i+1]
        elif ops[i] == "-":
            ans -= numbers[i+1]
    print(["Invalid Equation", "Valid Equation"][ans == numbers[3]])
