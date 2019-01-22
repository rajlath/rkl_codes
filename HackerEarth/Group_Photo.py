
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 19:42:34
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

nb_students = int(input())
widths = []
height = set()
students = []
for _ in range(nb_students):
    w, h = read_ints()
    students.append([w, h])
    widths.append(w)
    height.add(h)
total_width = sum([x[0] for x in students])
for i in students:
    ht = max([x for x in list(height) if x != i[1]])
    w  = total_width - i[0]
    print(ht * w)

