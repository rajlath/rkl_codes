
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 14:31:28
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

def is_acronym(w):
    num = defaultdict(int)
    for iw in w:
        num[iw] += 1
    valid = True
    for i in num.keys():
        valid &= num[i] <= firsts[i]
    start = w[0]
    valid &= num[start] < firsts[start]
    return valid




nb_words = read_int()
words = []
firsts= defaultdict(int)
for _ in range(nb_words):
    ins = read_str()
    words.append(ins)
    firsts[ins[0]] += 1

result = 0
for w in words:
    result += is_acronym(w)
print(result)

