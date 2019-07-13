'''
Given an array A of n integers, find the sum of f(a[i], a[j]) of all pairs (i, j)
such that (1 <= i < j <= n).
f(a[i], a[j]):       If | a[j]-a[i] | > 1
                        f(a[i], a[j]) = a[j] - a[i]
                        Else  if | a[j]-a[i] | <= 1
                        f(a[i], a[j]) = 0

Input:
The first line of the input contains T denoting the number of test cases.
For each test case, the first line contains integer n denoting the size of the array A,
followed by n space separated integers denoting the element of array A.

Output:
For each test case, the output is an integer denoting the sumof f(a[i],a[j]) of all pairs.

Constraints:
1<=T<=100
1<=n<=50

Example:
Input:
2
4
6 6 4 4
5
1 2 3 1 3
Output:
-8
4

Explanation:
1. All pairs are: (6 - 6) + (4 - 6) + (4 - 6) + (4 - 6) + (4 - 6) + (4 - 4) = -8
2. The pairs that add up are: (3, 1), (3, 1) to give 4, rest all pairs according to condition gives 0.
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 10:44:02
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
    lens = RI()
    arrs = RMI()
    ans = 0
    for i in range(lens):
        for j in range(i+1, lens):
            iv = arrs[i]
            jv = arrs[j]
            if abs(jv - iv) > 1:
                ans += jv - iv
            elif abs(jv - iv) <= 1:
                ans += 0
    print(ans)

