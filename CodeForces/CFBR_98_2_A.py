
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 11:45:12
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


ins = [x for x in input()]
turns = 0
done  = 0
while ins:
    curr = ins.pop()
    if len(ins) > 0:
        if curr == ins[-1]:
            done += 1
            if done == 5:
                turns += 1
                done = 0
        else:
            turns += 1
            done = 0
    else:
        turns += 1
print(turns)

from itertools import groupby
print (sum((len(list(j))-1)/5 + 1 for i, j in groupby(input())))

l=list(input())
t=l[0]
ans=1
ii=0
for x in l:
    if ii==5 or x!=t: ans+=1; ii=1; t=x
    else: ii+=1
print(ans)