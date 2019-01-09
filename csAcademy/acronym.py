
# -*- coding: utf-8 -*-
# @Date    : 2018-10-25 16:14:18
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

from collections import Counter

nb_words = read_int()
words  = [read_str() for _ in range(nb_words)]
fword  = Counter([x[0] for x in words])
print(fword)
cnt = 0
for i in words:
    curr_counter = Counter(i[1:])
    print(curr_counter)
    if all(curr_counter[j]<= fword[j] for j in curr_counter):
            cnt += 1
print(cnt)

