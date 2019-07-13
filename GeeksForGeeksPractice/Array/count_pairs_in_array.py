'''
Given an array of integers arr[0..n-1], count all pairs (arr[i], arr[j]) in it
such that i*arr[i] > j*arr[j], 0 =< i < j < n.

Example:

Input: arr[] = {5, 0, 10, 2, 4, 1, 6}

Output: 5

Explanation:

Pairs which hold condition i*arr[i] > j*arr[j] are
(10, 2) (10, 4) (10, 1) (2, 1) (4, 1)
Input:

The first line of input contains T denoting the no. of test cases .
Then T test cases follow .
The first line of each test case contains an Integer N and the next line
contains N space separated values of the array A[ ] .


Output:

For each test case output the required result in a new line.


Constraints:

1<=T<=100
1<=N<=100
1<=A[ ] <=1000


Example:

Input:

2
7
5 0 10 2 4 1 6
4
8 4 2 1

Output:
5
2
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-25 18:06:34
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
    #arrs = [i * j for i, j in enumerate(arrs)]
    result = 0
    for i in range(lens):
        for j in range(i+1, lens):
            if i * arrs[i] > j * arrs[j]:
                result += 1
    print(result)

