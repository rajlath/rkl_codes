# -*- coding: utf-8 -*-
# @Date    : 2019-01-31 20:49:00
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


from collections import defaultdict
nb_dish , nb_customer = read_ints()
dish_qty = read_ints()
costs    = read_ints()
dishes = {}
cost_indx = defaultdict(list)
for i in range(nb_dish):
    dishes[i+1] = dish_qty[i]
for i in range(nb_dish):
    cost_indx[costs[i]].append(i+1)
for i in range(nb_customer):
    billed = 0
    ordered, qty = read_ints()
    if qty <= dishes[ordered]:
        billed += costs[ordered] * qty
        dishes[ordered] -= qty
    else:
        billed =  dishes[ordered] * costs[ordered]
        balance = qty - dish[ordered]
        dishes[ordred] = 0
        for sorted(cost_index.keys())






