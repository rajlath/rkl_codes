
# -*- coding: utf-8 -*-
# @Date    : 2019-01-22 18:58:14
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



lens = int(input())
stud_pos = input()
stud_fin = ''
studs = [stud_pos[0+i:2+i] for i in range(0, lens, 2)]
cnts = 0
for i in studs:
    if i in ["XX", "xx"]:
        cnts += 1
        stud_fin += "Xx"
    else:
        stud_fin += i
print(cnts)
print(stud_fin)

n = int(input())
s = input()
c1 = s.count('x')
c2 = s.count('X')
s = s.replace('x', 'X', max(0, (c1 - c2) // 2))
s = s.replace('X', 'x', max(0, (c2 - c1) // 2))
print(abs(c2 - c1) // 2)
print(s)