
# -*- coding: utf-8 -*-
# @Date    : 2019-05-02 13:56:40
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
import random
from collections import Counter

sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]
'''
def is_it_ugly(s, n):
    for i in range(1, n):
        if abs( ord(s[i]) - ord(s[i -1]) ) == 1:
            return True
    return False

nb_test = RI()
for _ in range(nb_test):
    count= Counter(input())
    candidate = list(count.keys())
    valid='No answer'
    for _ in range(1000):
        random.shuffle(candidate)
        if not is_it_ugly(candidate,  len(candidate)):
            valid = ''.join([count[x] * x for x in candidate])
            break
    print(valid)
'''
nb_test = RI()
for _ in range(nb_test):
    curr = sorted(input())
    odds = ''
    evens= ''
    for x in curr:
        if ord(x)%2:odds += x
        else:evens += x
    ans = "No answer"
    if len(odds) == 0: ans=evens
    if len(evens)== 0: ans=odds
    if odds and evens:
        if abs( ord(odds[-1]) - ord(evens[0]) ) != 1: ans = odds + evens
        if abs( ord(odds[0]) - ord(evens[-1]) ) != 1: ans = evens+ odds
    print(ans)


