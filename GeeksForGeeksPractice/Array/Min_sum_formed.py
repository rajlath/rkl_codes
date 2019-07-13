'''
Given an array of digits (values are from 0 to 9),
find the minimum possible sum of two numbers formed from digits of the array.
All digits of given array must be used to form the two numbers.

Input:

The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow.
First line of each test case contains an integer N denoting the size of the array.
Next line of each test contains N space seperated integers denoting the elements of the array.


Output:

For each test case output a single line containing the required sum.


Constraints:

1<=T<=100
1<=N<=50
Example:

Input

2
6
6 8 4 5 2 3
5
5 3 0 7 4

Output

604
82

Explanation:

Test Case 1-

The minimum sum is formed by numbers
358 and 246
Test Case 2 -

The minimum sum is formed by numbers
35 and 047
'''


# -*- coding: utf-8 -*-
# @Date    : 2019-06-25 17:12:09
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
import heapq
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
    elem = RMI()
    heapq.heapify(elem)
    one = []
    two = []
    i = 1
    while elem:
        if i:
            one.append(heapq.heappop(elem))
            i = 1 - i
        else:
            two.append(heapq.heappop(elem))
            i = 1 - i
    ones = int("".join(map(str, one)))
    twos = int("".join(map(str, two)))
    print(ones + twos)





