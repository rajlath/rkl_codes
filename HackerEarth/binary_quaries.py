# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:24:00 2017

@author: rinfo
"""

noe, noq = [int(x) for x in input().split()]
binarr   = [int(x) for x in input().split()]
 
for _ in range(noq):
    arr = [int(x) for x in input().split()]
    if arr[0] == 1:
        pos = arr[1]-1
        binarr[pos] = not binarr[pos]
    else:
        l, r = arr[1]-1, arr[2]-1
        print(["EVEN","ODD"][binarr[l:r][-1]])
        
    
