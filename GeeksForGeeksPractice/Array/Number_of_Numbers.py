'''
Given an array A[]  of n elements.
Your task is to complete the Function num which returns an integer denoting the total number
of times digit k appears in the whole array.

For Example:

A[]={11,12,13,14,15}, k=1

Output=6 //Count of the digit 1 in the array


Input:
The first line of input contains an integer T denoting the no of test cases.
Then T test cases follow.
The first line of each test case contain an integer n denoting the size of the array A[].
Then in the second line are n space separated values of the array A[] .
In the third line of each test case contains an integer k, which is the digit to be counted.


Output:
For each test case in a new line print the number of elements counted.


Constraints:
1<=T<=100
1<=n<=20
1<=A[]<=1000


Example(To be used for expected output):
Input:
2
5
11 12 13 14 15
1
4
0 10 20 30
0

Output:
6
4
'''



# -*- coding: utf-8 -*-
# @Date    : 2019-06-25 18:55:37
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


''' This is a function problem.You only need to complete the function given below '''
# Your task is to complete this function
# Function should return an integer
def num(arr, n, k):
    # Code here
    return "".join(map(str,arr)).count(str(k)) # added this line only