# -*- coding: utf-8 -*-
# @Date    : 2018-09-21 20:07:28
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    :http://codeforces.com/contest/1047/problem/C
# @Version : 1.0.0
# adopted from solution by Monster_ixx
from sys import stdin
from functools import reduce
from math import gcd

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

n = read_int()
arr = read_ints()
gc_d= 0
gc_d= reduce(lambda gc_d,x : gcd(gc_d, x), arr)
vis = [0] * (max(arr)+10)
pri = [0] * (max(arr)+10)
mx  = min_val
for i in range(n):
    arr[i]//= gc_d
    vis[arr[i]] += 1
    mx = max(mx, arr[i])
ans = n
for i in range(2, mx+1):
    tmp = 0
    if not pri[i]:
        j = i
        while j < (mx+1):
            tmp += vis[j]
            pri[i] = 1
            ans = min(ans, n-tmp)
            j += i
print(-1 if ans==n else ans)

















