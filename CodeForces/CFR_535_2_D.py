
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 20:20:26
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

lens = read_int()
ins  = [x for x in input()] +["-"]

move = 0
ans  = ins[0]
for i in range(1, lens):
    if ins[i-1] != ins[i]:
        continue
    else:
        move +=1
        for j in "RGB":
            if j != ins[i-1] and j!= ins[i+1]:
                ins[i] = j
print(move)
print("".join(ins[:-1]))


