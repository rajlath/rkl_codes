
# -*- coding: utf-8 -*-
# @Date    : 2018-09-24 09:24:59
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    :
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

'''
Sample Input:
1
8
LLPLLPPL
2 3 4 1 2 1 5 3
Sample Output:
7
'''
nb_test = read_int()
for _ in range(nb_test):
    nb_months = read_int()
    profit_loss = [x for x in input()]
    vals = [int(x) for x in input().split()]
    values      = [v if profit_loss[i]=="P" else -1*v for i, v in enumerate(vals)]
    max_so_far =  values[0]
    max_over_all= values[0]

    for i in range(1, nb_months):
        max_so_far = max(values[i], max_so_far + values[i])
        max_over_all=max(max_over_all, max_so_far)

    print(max_over_all)

