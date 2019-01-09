
# -*- coding: utf-8 -*-
# @Date    : 2018-11-28 09:53:46
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


nb_test = read_int()
for _ in range(nb_test):
    lens = read_int()
    logs = read_str()
    valid = 0
    ans = "MAYBE YOU ARE SAFE"
    for i in logs:
        if i is "+":
            valid += 1
        elif i is "-":
            valid -= 1
            if valid < 0:
                ans =  "FIND A NEW JOB"
                break
        else:
            ans =  "FIND A NEW JOB"
            break

    print(ans)
