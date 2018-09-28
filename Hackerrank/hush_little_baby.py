
# -*- coding: utf-8 -*-
# @Date    : 2018-09-22 15:54:51
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.hackerrank.com/contests/recode-2/challenges/hush-little-baby
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

'''
7 9
3 4 1 7 8 2 6
1 2
1 3
1 4
4 5
2 3
3 4
3 5
3 6
6 7
'''
from collections import defaultdict
nb_city, nb_road = read_ints()
city_gift = [0] + read_ints()
connection = defaultdict(list)
tot_gifts  = defaultdict(int)
visited    = [0] * (nb_city+1)
for i in range(nb_road):
    s, t = read_ints()
    connection[s].append(t)
    connection[t].append(s)
    tot_gifts[s] += city_gift[t]
    tot_gifts[t] += city_gift[s]

for i in range(1, nb_city+1):
    tot_gifts[i] += city_gift[i]
max_gift = tot_gifts[1]
j = 1
for i in range(2, nb_city + 1):
    if tot_gifts[i] > max_gift:
        max_gift = tot_gifts[i]
        j = i

visited[j] = 1
for y in connection[j]:
    visited[y] = 1
k = max_gift
max_gift = -1
for i in range(1, nb_city+1):
    if not visited[i] and city_gift[i] > max_gift:
        max_gift = city_gift[i]
if max_gift != -1: k += max_gift
print(k)





