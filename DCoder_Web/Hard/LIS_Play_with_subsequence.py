'''
Play with Sequences and Subsequence
Problem statement
Rick is Professor at Zing University. He teaches Maths there. One day he was teaching Sequence, suddenly he came up on a problem, which was taking alot of time.Cody being a Coder, decided to solve the problem using code, so he just put his mobile out , opened the Dcoder app and started coding. Meanwhile his teacher was solving the problem on board, the problem statment was like, There is a sequence of n integers, you have to find the longest increasing subsequence of it, in case more than 1 sequence exists, output the earliest one.
Now this becomes a "Coder vs Mathematician" problem, being a coder lets help Cody in solving the problem first.
Input
First line of the input contains number of elements in the sequence n, next line contains n space separated integers.
Output
Output the longest increasing subsequence in the given sequence.
Constraint
1≤n≤10000
1≤intger values≤100000
Sample Input
5
4 2 6 3 8
Sample Output
4 6 8
'''
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 16:53:30
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
def read_str_list(): return [x for x in stdin.readline().split().split()]

# Python implementation to
# find longest increasing
# subsequence
# in O(n Log n) time.

# Binary search
def GetCeilIndex(arr, T, l, r, key):

    while (r - l > 1):

        m = l + (r - l)//2
        if (arr[T[m]] >= key):
            r = m
        else:
            l = m

    return r

def LongestIncreasingSubsequence(arr,n):

    # Add boundary case,
    # when array n is zero
    # Depend on smart pointers

    # Initialized with 0
    tailIndices=[0 for i in range(n+1)]

    # Initialized with -1
    prevIndices=[-1 for i in range(n+1)]

    # it will always point
    # to empty location
    len = 1
    for i in range(1, n):

        if (arr[i] < arr[tailIndices[0]]):

            # new smallest value
            tailIndices[0] = i

        elif (arr[i] > arr[tailIndices[len-1]]):

            # arr[i] wants to extend
            # largest subsequence
            prevIndices[i] = tailIndices[len-1]
            tailIndices[len] = i
            len += 1

        else:

            # arr[i] wants to be a
            # potential condidate of
            # future subsequence
            # It will replace ceil
            # value in tailIndices
            pos = GetCeilIndex(arr, tailIndices, -1,
                                len-1, arr[i])

            prevIndices[i] = tailIndices[pos-1]
            tailIndices[pos] = i

    print("LIS of given input")
    i = tailIndices[0]
    while(i < len):
        print(arr[i] , " ",end="")
        i = prevIndices[i]
    print()
    return len

nb_elem = read_int()
elements= read_ints()
m = [max_val] * (nb_elem + 1)
LongestIncreasingSubsequence(elements,nb_elem)











