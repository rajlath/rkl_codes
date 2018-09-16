'''
Problem statement
You have an array of length N. A subarray is called "Prime Subarray" if it contains only prime numbers.You have to find the maximum length of such Prime subarray in a given array.
Input
First line contains T , denoting number of test cases.
Each test case contains two lines:
1.First line contains an integer N denoting the size of the array.
2.Second line contains N space separated integers denoting the value of array elements.
Output
For each test case, print the maximum length of Interesting subarray. If no such subarray exist,print -1.
Constraint
1<=T<=5
1<=N<=10^5
1<=A[i]<=10^6.
Sample Input
1
7
1 3 4 5 7 2 8
Sample Output
3
'''

# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 13:16:53
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

def prime_hive(n):
    primes = [True] * (n + 5)
    primes[0] = False
    primes[1] = False
    for i in range(2, n):
        if primes[i]:
            for j in range(i+i, n, i):
                primes[j] = False
    return primes

primes = prime_hive(10 ** 6 + 5)
nots = read_int()
for _ in range(nots):
    lens = read_int()
    arrs = read_ints()
    max_len = 0
    curr_cnt= 0
    for i in range(lens):
        if primes[arrs[i]]:
            curr_cnt += 1
            max_len = max(max_len, curr_cnt)
        else:
            curr_cnt = 0
    max_len = max(max_len, curr_cnt)
    print(max_len if max_len > 0 else -1)




