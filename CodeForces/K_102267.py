
# -*- coding: utf-8 -*-
# @Date    : 2019-08-25 19:19:53
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

INT_SIZE = 32
# function to find the OR_SUM
def ORsum(arr, n):
    # create an array of size 32
    # and store the sum of bits
    # with value 0 at every index.
    zerocnt = [0 for i in range(INT_SIZE)]

    for i in range(INT_SIZE):
        for j in range(n):
            if not (arr[j] & (1 << i)):
                zerocnt[i] += 1

    # for each index the OR sum contributed
    # by that bit of subset will be 2^(bit index)
    # now the OR of the bits is 0 only if
    # all the ith bit of the elements in subset
    # is 0.
    ans = 0
    for i in range(INT_SIZE):
        ans += ((2 ** n - 1) - (2 ** zerocnt[i] - 1)) * 2 ** i

    return ans

lens = RI()
vals = RMI()
print(ORsum(vals, lens))