
# -*- coding: utf-8 -*-
# @Date    : 2018-09-18 11:35:59
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

'''
input
3
7
1
6
5
output
7 13
'''
nb_benches = read_int()
incoming  = read_int()
on_benches = []
for _ in range(nb_benches):
    on_benches.append(read_int())

max_ans =  max(on_benches) + incoming
for _ in range(incoming):
    on_benches[on_benches.index(min(on_benches))] += 1
    #print(on_benches)
min_ans = max(on_benches)
print(min_ans, max_ans)



