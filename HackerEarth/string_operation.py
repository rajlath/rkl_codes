
# -*- coding: utf-8 -*-
# @Date    : 2019-01-18 19:16:35
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

initial = list(input())
final   = initial
nb_q = int(input())
for _ in range(nb_q):
    ind, ch = [x for x in input().split()]
    final[int(ind)-1] = ch
print("".join(final))
nb_m = int(input())
for _ in range(nb_m):
    l, r = read_ints()
    l-=1
    r-=1
    final= final[:l] + final[l:r+1][::-1] + final[r+1:]

print("".join(final))
print(sum(1 for x , y in zip(initial, final) if x == y))



