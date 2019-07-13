'''
Given an array if ‘n’ positive integers, count number of pairs of integers in the array that have the sum divisible by 4.

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each test-case has two lines of the input, the first line contains an integer denoting the size of an array N and the second line of input contains N positive integers.
Output:

Print the number of pairs of integers in the array that have the sum divisible by 4.
Constraints:

1<=T<=100

1<=N<=100

1<=arr[]<=1000
Example:

Input:

2

5

2 2 1 7 5

5

2 2 3 5 6

Output:

3

4

Explanation:

Testcase 1: (2,2), (1,7) and(7,5) are the 3 pairs.

Testcase 2: (2,2), (2,6), (2,6), (3,5) are the 4 pairs.
'''


# -*- coding: utf-8 -*-
# @Date    : 2019-06-26 15:10:04
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
    counts = 0
    for i in range(lens):
        for j in range(i+1, lens):
            if (arrs[i] + arrs[j]) % 4 == 0:counts += 1
    print(counts)



