# -*- coding: utf-8 -*-
# @Date    : 2018-09-03 08:46:01
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : http://codeforces.com/contest/1037/problem/D
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

nb_vertices = read_int()

graph = [set() for vert in range(nb_vertices+2)]
for _ in range(nb_vertices - 1):

    src,des = read_ints()
    graph[src].add(des)
    graph[des].add(src)

vertices = read_ints()
ans = "Yes"
if vertices[0] is not 1:
    ans = "No"
else:
    i = 1
    j = 0
    while j < nb_vertices and i < nb_vertices:
        if vertices[j] in graph[i] : i += 1
        else: j+= 1
    if j is not nb_vertices and i is not nb_vertices:
        ans = "No"
print(ans)






