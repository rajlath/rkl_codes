'''
Given an array of size N consisting of only 0's and 1's ,which is sorted in such a manner that all
the 1's are placed first and then they are followed by all the 0's. You have to find  the count of all the 0's.


Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
The first line of each test case contains an integer N, where N is the size of the array A[ ].
The second line of each test case contains N space separated integers of all 1's follwed by all the 0's,
denoting elements of the array A[ ].


Output:
Print out the number of 0's in the array.


Constraints:
1 <= T <= 100
1 <= N <= 30
0 <= A[i] <= 1


Example :

Input:
3
12
1 1 1 1 1 1 1 1 1 0 0 0
5
0 0 0 0 0
6
1 1 1 1 1 1


Output:
3
5
0
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 11:04:10
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
    if 0 in arrs:
        index = arrs.index(0)
        print(lens - index)
    else:
        print(0)