
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 14:04:37
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


nb_test = int(input())
for _ in range(nb_test):
    s = input()
    j = 0
    count = 0
    while j < len(s):
        if((s[j]=='W') and ((j>0 and s[j-1]=='B') or (j>1 and s[j-2]=='B') or (j<len(s)-1 and s[j+1]=='B') or (j<len(s)-2 and s[j+2]=='B')) ):
            count += 1
        j += 1
    print(count)





