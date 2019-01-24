
# -*- coding: utf-8 -*-
# @Date    : 2019-01-22 18:58:14
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
ins = input()
curr= 0
while re.findall(r"(.)\1", ins):
    ins1 = re.sub(r"(.)\1",'',ins, 1)
    if ins1 == ins:break
    else:
        curr += 1
        ins = ins1
if curr%2:
    print("YES")
else:
    print("NO")