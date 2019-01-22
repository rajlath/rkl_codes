
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 12:54:23
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


dicts = {1:".,?!1", 2:"abc2", 3:"def3", 4:"ghi4", 5:"jkl5", 6:"mno6", 7:"pqrs7", 8:"tuv8", 9:"wxyz9", 10:"_0"}
char = [".,?!1", "abc2", "def3", "ghi4", "jkl5", "mno6", "pqrs7", "tuv8", "wxyz9", "_0"]

def get_location(x):
    for i, v in enumerate(char):
        if x in v:
            return i + 1
nb_test = int(input())
for _ in range(nb_test):
    ins = input()
    pos = get_location(ins[0])
    last_pos = pos
    strokes  = dicts[pos].index(ins[0])+1
    if pos != 1:
        strokes += 1
    for i in ins[1:]:
        pos = get_location(i)
        if pos != last_pos:
            last_pos = pos
            strokes += 1
        strokes += dicts[pos].index(i) + 1
    print(strokes)



