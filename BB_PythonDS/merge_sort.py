
# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 13:29:38
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : Benjamin Baka PythonDSandAlgo Examples
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

def mergeSort(A):
    #base case if the input array is one or zero just return.
    if len(A) > 1:
        # splitting input array
        print('splitting ', A )
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        #recursive calls to mergeSort for left and right sub arrays
        mergeSort(left)
        mergeSort(right)


        #initalizes pointers for left (i) right (j) and output array (k)
        # 3 initalization operations
        i = j = k = 0
        #Traverse and merges the sorted arrays
        while i <len(left) and j<len(right):
            # if left < right comparison operation
            if left[i] < right[j]:
                # if left < right Assignment operation
                A[k]=left[i]
                i=i+1
            else:
                #if right <= left assignment
                A[k]= right[j]
                j=j+1
                k=k+1
                
        while i<len(left):
            #Assignment operation
            A[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            #Assignment operation
            A[k]=right[j]
            j=j+1
            k=k+1
    print('merging ', A)
    return(A)

print(mergeSort([359, 67, 132, 411, 9, 109]))



