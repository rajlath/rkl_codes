
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 08:46:17
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/substring-in-blocks-335081c2/
# @Version : 1.0.0

'''
12
abcbbcdefxyz
6
abz 3 1
baz 3 2
abbby 3 2
adef 3 2
abxc 5 2
acdxyz 5 2
'''

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

def cpp_upper_bound(arr, n, x):
    """
    implement upper_bound as in cpp
    Returns an iterator pointing to the first element in the range [first,last)
    which compares greater than val.
    type: list arr
    type: n    length of the list
    type: x    value to be adjudged
    rets: int
    """
    left = 0
    rite = n
    while left < rite:
        mid = (left + rite) // 2
        if x >= arr[mid]:
            left = mid + 1
        else:
            rite = mid
    return left

def cpp_lower_bound(arr, n, x):
    """
    implements lower_bound as in cpp
    Returns an iterator pointing to the first element in the range [first, last]
    which does not compare less than val.
    The elements in the range shall already be sorted or at least partitioned with respect to val.

    type: list   arr
    type: int    n  length of the list
    type: int    x  value to be adjudged
    rets: int    p  position of x in the list
    """
    left, rite = 0, n
    while left < rite:
        mid = (left + rite)//2
        if x <= arr[mid]:
            rite = mid
        else:
            left = mid + 1
    return left

lens = read_int()
strs = read_str()
v = [ord(x) - ord("a") + 1 for x in strs]
nb_qry= read_int()
ans = "No"
for _ in range(nb_qry):
    s, b, k = read_strs()
    b, k = int(b), int(k)
    tp   = (lens + b -1) // b
    use = {}
    for i in s:
        io = ord[i] - ord['a']
        pos = cpp_upper_bound(v, lens, io)
        if pos == lens:
            break
        else:
            pos = v[io][pos]





