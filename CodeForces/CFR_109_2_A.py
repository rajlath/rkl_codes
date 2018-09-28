
# -*- coding: utf-8 -*-
# @Date    : 2018-09-27 13:25:36
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


nb_scores = read_int()
scores    = read_ints()
min_score = scores[0]
amazing = 0
for i in range(1, nb_scores):
    amazing += scores[i] > max(scores[:i]) or scores[i] < min(scores[:i])
print(amazing)




