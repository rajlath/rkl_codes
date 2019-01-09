
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 08:46:22
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


nb_shop, has_amt = read_ints()
prices  = read_ints()
sums = sum(prices)
ans  = 0
size = nb_shop
while size:
    curr, has_amt = divmod(has_amt, sums)
    ans += curr * size
    sums = 0
    for i in range(nb_shop):
        if sums + prices[i] > has_amt:
            prices[i] = 0
            size -= 1
        sums += prices[i]
print(ans)