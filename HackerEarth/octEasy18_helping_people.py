
# -*- coding: utf-8 -*-
# @Date    : 2018-10-06 10:57:53
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

ins = read_str()
ans = "valid"

for i  in range(1, len(ins)):
    if i in [3, 6, 7]: continue
    elif i == 2:
        if ins[i] in "AEIOUY":
            ans = "invalid"
            break
    else:
        #print(i, ins[i], ins[i-1])
        if (int(ins[i]) + int(ins[i-1]))%2==1:
            ans = "invalid"
            break
print(ans)



