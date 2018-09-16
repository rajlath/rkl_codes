'''
Arrays and Merging
Problem statement
Cody's girlfriend loves Arrays.She is a sorted girl, hence likes sorted arrays. Being a Coder Cody decide to give her some sorted arrays but this time she demanded even more, she said she needed kth smallest element in the union of the arrays, now cody is really puzzled. He don't have an idea to do this, you need to help Cody making a program to do so.
Input
First line of the input contains integer m, follows by m integers separated by space, elements of 1st array
Next line contains integer n, follows by n integers separated by space, elements of 2nd array.Last line contains k.
Output
Print the kth smallest element of the merged array.
Constraint
1≤m,n≤100
1≤ element of array≤100000
Sample Input
10
3 28 99 108 112 123 291 543 934 1221
3
5 104 111
9
Sample Output
123
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

lenA = read_int()
A    = read_ints()
lenB = read_int()
B    = read_ints()
k    = read_int()

i, j = 0, 0
merged = []
while (i < (lenA)) and (j < (lenB)):
    #print(i, j, merged)
    if A[i] <= B[j]:
        merged.append(A[i])
        i += 1
    else:
        merged.append(B[j])
        j += 1


while i < lenA:
        merged.append(A[i])
        i  += 1

while j < lenB:
        merged.append(B[j])
        j  += 1

print(merged[k-1])








