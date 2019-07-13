
# -*- coding: utf-8 -*-
# @Date    : 2019-07-03 15:14:32
# @Author  :  (oorja.halt@gmail.com)
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
import sys
def get_min_coins(coins, nbcoin, amount):
    table = [max_val] * (amount + 1)
    table[0] = 0
    for i in range(1, amount+1):
        for j in range(nbcoin):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if sub_res != max_val and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1
    return table[amount]


nb_coins, amount = RMI()
denoms = RMI()
print(get_min_coins(denoms, nb_coins, amount))


