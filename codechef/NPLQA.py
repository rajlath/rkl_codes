
# -*- coding: utf-8 -*-
# @Date    : 2018-09-22 20:22:55
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

'''
2
5 3
2 12 11 7 10
10 2
4 9 2 3 8 40 29 3 6 5
'''
nb_test = int(input())
for _ in range(nb_test):
    noj, noro = [int(x) for x in input().split()]
    jwellery  = sorted([int(x) for x in input().split()], reverse=True)
    print(sum(jwellery[:noro]))