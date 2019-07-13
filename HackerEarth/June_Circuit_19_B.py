
# -*- coding: utf-8 -*-
# @Date    : 2019-06-25 07:17:28
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

def get_values(N, M):
    has, can = N, M
    dp = [0] * (has + 1 + can)
    dp[0] = 0
    dp[1] = 1
    for i in range(1, has + can):
        if i - can >= 0 and dp[i - can] % 2 == 0:
            dp[i] = 1
        if i - 1 >= 0 and dp[i - 1]  % 2 ==  0:
            dp[i] = 1
    if dp[has] % 2 == 1:return "ARPA"
    else:return "Dishant"

'''
nb_Test = int(input())
for _ in range(nb_Test):
   has, can = RMI()
   dp = [0] * (has + 1 + can)
   dp[0] = 0
   dp[1] = 1
   for i in range(1, has + can):
       if i - can >= 0 and dp[i - can] % 2 == 0:
           dp[i] = 1
       if i - 1 >= 0 and dp[i - 1]  % 2 ==  0:
           dp[i] = 1
   if dp[has] % 2 == 1:print("ARPA")
   else:print("Dishant")
'''
N = 24
if N%2:
    print("For even numbers : {}".format(N))
else:
    print("For odd  numbers : {}".format(N))
for i in range(1, 10):
    res = get_values(N, i)
    cur = "Even"
    if i%2:cur="ODD"
    mod = N % i
    print("{} {} {} {} ".format(i, cur, mod, res))



