
# -*- coding: utf-8 -*-
# @Date    : 2018-09-28 09:18:53
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


lens , sum_needed =  read_ints()
if lens == 1 and sum_needed == 0:
    print(0,0)
elif 9 * lens < sum_needed or sum_needed == 0:
    print(-1, -1)
else:
    answer = 10 ** (lens - 1)
    for i in range(sum_needed - 1):
        answer += 10 ** (i//9)
        #print(answer)
    print(answer, end=" ")
    answer = 0
    for i in range(sum_needed):
        answer += 10 ** (lens - 1 - i//9)
    print(answer, end=" ")


