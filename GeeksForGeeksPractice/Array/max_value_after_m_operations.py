'''
Given an array of size N with all initial values as 0, write a program to perform following M range increment
operations as shown below:

increment(a, b, k) : Increment values from 'a' to 'b' by 'k'.

After M operations, calculate the maximum value in the array.
Input:
First line of input contains a single integer T which denotes the number of test cases.
T test cases follows.
First line of each test case contains two space separated integers N and M.
Next M lines of each test case contains three space separated integers a , b and k.

Output:
For each test case print the maximum element in the array after M increment operations.

Constraints:
1<=T<=100
1<=N<=105
1<=M<=1000
0<= a,b <= N-1

Example:
Input:
2
5 3
0 1 100
1 4 100
2 3 100
4 3
1 2 603
0 0 286
3 3 882
Output:
200
882
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 13:18:45
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
    arr_lens , nb_operation = RMI()
    lefts = []
    rites = []
    k_val = []
    rets  = [0] * arr_lens
    for i in range(nb_operation):
        left, rite, kval = RMI()
        for i in range(left, rite+1):
            rets[i] += kval
    print(max(rets))




