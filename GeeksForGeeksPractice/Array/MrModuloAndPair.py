'''
Mr. Modulo comes up with another problem related to modulo and this time he is interested in finding all the possible pairs a and b in the array a[] such that a % b = k where k is a given integer. The array given will have distinct elements.
You are required to print how many such pairs exist.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains two integers n and k, where n is the number of elements in the array a[]. Next line contains space separated n elements in the array a[].

Output:
Print an integer which is the total number of such pairs in the array.

Constraints:
1<=T<=10
2<=n<=1000
1<=k<=1000
1<=a[i]<=100000

Example:
Input:
1
5 3
2 3 5 4 7

Output:
4
'''


# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 17:07:50
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
    lens, mods = RMI()
    arrs = RMI()
    counts = 0
    for i in range(lens):
        for j in range(lens):
            if i != j:
                if arrs[i] % arrs[j] == mods :
                    counts += 1
    print(counts)

