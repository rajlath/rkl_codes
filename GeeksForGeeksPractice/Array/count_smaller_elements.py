'''
Given an array A of positive integers. Count number of smaller elements on right side of each array.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N,N is the size of array. The second line of each test case contains N input arr[i].

Output:
Print the countSmaller array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
1 <= Ai  <= 108

Example:
Input:
2
7
12 1 2 3 0 11 4
5
1 2 3 4 5

Output:
6 1 1 1 0 1 0
0 0 0 0 0

Explanation:
Testcase 1: 6 elements are greater than 1 on its right side in original array. Similarly 1 element is greater than 4 on its right side in original array.
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 12:06:59
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

import bisect

nb_test = RI()
for _ in range(nb_test):
    lens = RI()
    arrs = RMI()
    answer = [0] * lens
    bis = []
    for i in range(lens-1, -1, -1):
        idx = bisect.bisect_left(bis, arrs[i])
        print(idx)
        bis.insert(idx, arrs[i])
        print(bis)
        answer[i] = idx
    print(*answer)