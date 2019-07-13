
# -*- coding: utf-8 -*-
# @Date    : 2019-05-24 20:48:37
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


# Python3 Program to divide N segments
# into two non empty groups such that
# given condition is satisfied

# Structure to hold the elements of
# a segment
class segment:

    def __init__(self):
        self.l = None # left index
        self.r = None # right index
        self.idx = None # index of the segment

# Function to print the answer if
# it exists using the concept of
# merge overlapping segments
def printAnswer(v, n):
    seg = [segment() for i in range(n)]
    # Assigning values from the vector v
    for i in range(0, n):
        seg[i].l = v[i][0]
        seg[i].r = v[i][1]
        seg[i].idx = i

    # Sort the array of segments
    # according to right indexes
    seg.sort(key = lambda x: (x.r, x.idx))

    # Resultant array
    res = [0] * (n)

    # Let’s denote first group with 0 and
    # second group with 1 Current segment
    prev = 0

    # Assigning group 1 to first segment
    res[seg[prev].idx] = 0
    for i in range(1, n):
        # If the current segment overlaps
        # with the previous segment, merge it
        if seg[i].l <= seg[prev].r:
            # Assigning same group value
            res[seg[i].idx] = res[seg[prev].idx]
            seg[prev].r = max(seg[prev].r, seg[i].r)
        else:
            # Change group number and create # new segment
            res[seg[i].idx] = res[seg[prev].idx] ^ 1
            prev += 1
            seg[prev] = seg[i]
            # Check if one of the groups is # empty or not one,
            two = 0, 0
            for i in range(0, n):
                if not res[i]: one += 1
                else:
                     two += 1
                     # If both groups are non-empty
                     if one and two:
                         for i in range(0, n):
                             print(res[i] + 1, end = " ")
                             print()
                     else:
                         print("Not Possible")
# Driver Code i
if __name__ == "__main__":
    v = [[1, 2], [3, 4], [5, 6]]
    n = len(v)
    printAnswer(v, n)