'''
Given an array of integers, and an integer  ‘K’ ,
find the count of pairs of elements in the array whose sum is equal to 'K'.

Input:
First line of the input contains an integer T, denoting the number of test cases.
Then T test cases follow. Each test case consists of two lines.
First line of each test case contains 2 space separated integers N and K denoting
the size of array and the sum respectively.
Second line of each test case contains N space separated integers denoting the elements of the array.

Output:
Print the count of pairs of elements in the array whose sum is equal to the K.

Constraints:
1<=T<=50
1<=N<=50
1<=K<=50
1<=A[i]<=100

Example:
Input
2
4 6
1  5  7 1
4 2
1 1 1 1
Output
2
6
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-25 19:36:11
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
    lens, sums = RMI()
    arrs = RMI()
    pairs = set()
    counts = 0
    for i in arrs:
        pair = sums - i
        if pair >= 0:
            if pair in pairs:
                counts += 1
        pairs.add(pair)
    print(counts * 2)


