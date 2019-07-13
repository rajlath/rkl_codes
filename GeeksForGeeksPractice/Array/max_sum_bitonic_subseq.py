'''
Given an array of integers A. A subsequence of A is called Bitonic if it is first increasing then decreasing.

Input:
The first line contains an integer T denoting the no of test cases. Each test case consist of two lines. The first line contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array A[].

Output:
For each test case in a new line print the max sum bitonic subsequence.

Constraints:
1<=T<=100
1<=N<=50
1<=A[]<=100

Example:
Input:
2
6
80 60 30 40 20 10
9
1 15 51 45 33 100 12 18 9

Output:
210
194

Explanation:
Testcase2:
Input : A[] = {1, 15, 51, 45, 33, 100, 12, 18, 9}
Output : 194
Bi-tonic Sub-sequence are :
{1, 51, 9}
{1, 50, 100, 18, 9}
{1, 15, 51, 100, 18, 9}
{1, 15, 45, 100, 12, 9}
{1, 15, 45, 100, 18, 9} .. so on
Maximum sum Bi-tonic sub-sequence is 1 + 15 + 51 + 100 + 18 + 9 = 194


'''



# -*- coding: utf-8 -*-
# @Date    : 2019-06-28 07:38:16
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
    max_sum_increasing_seq = arrs[:]
    for i in range(lens):
        for j in range(0, i):
            if arrs[i] > arrs[j] and max_sum_increasing_seq[i] < max_sum_increasing_seq[j] + arrs[i]:
                max_sum_increasing_seq[i] = max_sum_increasing_seq[j] + arrs[i]
    max_sum_decreasing_seq = arrs[:]
    for i in range(1, lens + 1):
        for j in range(1, i):
            if arrs[-i] < arrs[-j] and max_sum_decreasing_seq[-i] < max_sum_decreasing_seq[-j] + arrs[-i]:
                max_sum_decreasing_seq[-i] = max_sum_decreasing_seq[-j] + arrs[-i]
    answer = min_val
    for i, j, k in zip(max_sum_increasing_seq, max_sum_decreasing_seq, arrs):
        answer = max(answer, i + j - k)
    print(answer)






