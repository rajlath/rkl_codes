
# -*- coding: utf-8 -*-
# @Date    : 2019-03-15 12:28:52
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


nb_test = RI()
for _ in range(nb_test):
    vowel = "aeiou"
    lens  = RI()
    counts = 0
    words = sorted(["".join(sorted(set(RW()))) for _ in range(lens)])
    table = dict()
    for w in words:
        table[w] = table.get(w, 0) + 1
    word = list(table.keys())
    if words[-1] == vowel:
        counts += sum(range(1, table[vowel]))
    for index, i in enumerate(word)    :
        for j in word[index+1:]:
            s = ''.join(sorted(''.join(set(i + j))))
            if s == vowel:
                counts += table[i] * table[j]
    print(counts)

