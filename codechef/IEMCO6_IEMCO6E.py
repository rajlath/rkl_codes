
# -*- coding: utf-8 -*-
# @Date    : 2018-11-12 07:56:34
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
nb_keys, nb_person = read_ints()
dicts = defaultdict(list)
keys  = []
for _ in range(nb_keys):
    keys.append(read_str())
    dicts[keys[-1][0]].append(keys[-1])
for _ in range(nb_person):
    person = read_str()
    first = person[0]
    if first not in dicts:
        print(0)
    else:
        cnt = 0
        for x in dicts[first]:
            if x.startswith(person):
                cnt += 1
        print(cnt)


