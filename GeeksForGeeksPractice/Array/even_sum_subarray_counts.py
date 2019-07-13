'''
Given an array  A[]  you have to  find the number of subarrays whose sum is an even number.


Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
The first line  of each test case contains an integer N, where N is the size of the array A[ ] .
Then Next line contains space seperated N value of the array A[ ].


Output:
For each test case in a new line, number of sub-arrays having even sum


Constraints:
1 <= T <= 200
1 <= N <= 100
1<= A[i] <=100



Example:

Input:
1
6
1 2  2  3  4 1

Output:
9


Explanation:
In the first test case the array  {1, 2, 2, 3, 4, 1} has 9 such possible subarrays-

These are-

{1, 2, 2, 3}          Sum = 8

{1, 2, 2, 3, 4}      Sum as  = 12

{2}                      Sum as  = 2 (At index 1)

{2, 2}                  Sum as Sum = 4

{2, 2, 3, 4, 1}      Sum as = 12

{2}                      Sum as  = 2 (At index 2)

{2, 3, 4, 1}          Sum as = 10

{3, 4, 1}              Sum as  = 8

{4}                      Sum as = 4

'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 11:52:20
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
    temp = [1, 0]
    result = 0
    sums   = 0
    for i in range(lens):
        sums = (sums + arrs[i] % 2 + 2) % 2
        temp[sums] += 1
    even, odds = temp[0], temp[1]
    result = result + (even * (even - 1)) // 2
    result = result + (odds * (odds - 1)) // 2
    print(result)