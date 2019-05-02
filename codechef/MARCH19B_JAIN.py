
# -*- coding: utf-8 -*-
# @Date    : 2019-03-15 11:45:36
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

def calc(s):
    return sum([x * (pow(2, i) for i, x in enumerate(s))])

nb_test = RI()
for _ in range(nb_test):
    cnt = RI()
    words= [RW() for _ in range(cnt)]
    vowel_count = []
    freq_count  = [0  for _ in range(32)]
    for i in range(len(words)):
        vowel = [0] * 5
        for j, v  in enumerate(words[i]):
            vowel["aeiou".index(v)] = 1
        num = 0
        for i, x in enumerate(vowel):
            num += x * pow(2, i)
        freq_count[num]+= 1
    res = 0
    for i in range(1, 31):
        for j in range(i+1, 32):
            if i | j == 31:
                res += freq_count[i] * (freq_count[j])
    res += freq_count[31] * (freq_count[31] - 1) // 2
    print(res)





