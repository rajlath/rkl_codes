'''
Problem statement
In a Parallel Universe, the iconic duo of Rose and Jack did not die due to the drowning of the Titanic and they are all set to marry next week. But before marrying, they need to complete a ritual unique to their universe. All persons are assigned a unique array, set of numbers.Before marriage, the couple needs to merge those array and set the elements in ascending order. This array will now be common to both of them and is known as the Couple Array. Given the array of Rose and Jack, print their Couple Array.
NOTE : The unique arrays of each person need not necessarily be sorted.
Input
The first line of input contains N, the number of elements in both the arrays.
The next two lines of input contain N space separated integers denoting the array of Rose
and Jack, respectively.
Output
Print the Couple Array with each element separated by a space

Constraint
1 ≤ N ≤ 1000
-1000 ≤ A[i] ≤ 1000
Sample Input
5
5 4 2 3 1
9 6 10 8 7
Sample Output
1 2 3 4 5 6 7 8 9 10
'''

# -*- coding: utf-8 -*-
# @Date    : 2018-09-09 20:14:41
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

def merge_array(r, jk):
    i = 0
    j = 0
    k = 0
    arr = [None] * (len(r) + len(jk))
    while i < len(r) and j < len(jk):
        if r[i] <= jk[j]:
            arr[k] = r[i]
            i += 1
        else:
            arr[k] = jk[j]
            j += 1
        k += 1
    while i < len(r):
        arr[k] = r[i]
        i += 1
        k += 1
    while j < len(jk):
        arr[k] = jk[j]
        j += 1
        k += 1
    return arr



read_int()
rose = sorted(read_ints())
jack = sorted(read_ints())
print(*merge_array(rose, jack))
