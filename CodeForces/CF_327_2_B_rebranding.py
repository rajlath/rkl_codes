
# -*- coding: utf-8 -*-
#! @Date    : 2018-09-05 13:15:44
#! @Author  : raj lath (oorja.halt@gmail.com)
#! @Link    : "https://codeforces.com/contest/591/problem/B"
#! @Version : 1.0.0

import os
from sys import stdin

max_val=int( 10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline()]
def read_str_list(): return [x for x in stdin.readline().split()]

from string import ascii_lowercase as lc
def main():
    alpha_indx = {x:y for x, y in zip(lc,lc)}
    str_len, nb_msger = read_ints()
    company_name = read_str()
    for _ in range(nb_msger):
        a, b = read_str_list()
        alpha_indx[a], alpha_indx[b] = b, a
    ans = ''
    for i in company_name:
        ans += alpha_indx[i]
    print(ans)




if __name__ == "__main__":
    main()

