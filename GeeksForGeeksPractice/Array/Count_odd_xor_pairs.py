'''
Given an array Arr[] of N integers. Write a program to find out number of pairs in array whose XOR is odd.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains a single integer N which denotes the size of array. Second line of each test case contains N space separated integers which denotes the elements of the array.

Output:
For each test case print the number of pairs in array whose XOR is odd.

Constraints:
1<=T<=100
1<=N<=1000
1<=Arr[i]<=1000

Example:
Input:
2
3
1 2 3
4
1 2 3 4
Output:
2
4
'''

# -*- coding: utf-8 -*-
# @Date    : 2019-06-27 10:44:19
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
    odds = len([x  for x in arrs if x & 1])
    even = lens - odds
    print(even * odds)