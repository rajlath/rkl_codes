#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rinfo
#
# Created:     31/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
nos, maxs = [int(x) for x in input().split()]
points = [0] * (maxs+1)
points[0] = 0
for i in range(nos):
    st, en = [int(x) for x in input().split()]
    for j in range(st,en+1):
        points[j] = 1
sums = sum([1 for x in points[1:] if x==0])
print(sums)
for i,v  in enumerate(points[1:]):
    if v == 0:print(i+1, end=" ")

