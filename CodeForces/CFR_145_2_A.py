
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 14:06:35
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

F = open('input.txt')
W = open("output.txt", "w")
I = lambda:[int(x) for x in F.readline().split()]
nb_hours , read_hours = I()
lights = I()
light_sorted = sorted(enumerate(lights), key=lambda x:x[1])
print(light_sorted[-read_hours][1], file=W)

print(' '.join(sorted(map(str, [u[0]+1 for u in light_sorted[nb_hours - read_hours:nb_hours]]))), file=W)

