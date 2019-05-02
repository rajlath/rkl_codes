
# -*- coding: utf-8 -*-
# @Date    : 2019-03-07 21:05:32
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


def valid_pairs(arr, n, k):
    freq = {i:0 for i in range(k)}
    for i in range(n):
        freq[arr[i]%k] += 1
    print(freq)
    ans = freq[0] //  2
    for i in range(1, k):
        if i in freq and abs(k - i) in freq:
            ans += freq[i] + freq[k - i] // 2
    return ans




nb_elem , k = RMI()
arr = RMI()
print(valid_pairs(arr, nb_elem,k))


