# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 15:56:32 2018
coded by : rinfo
"""
from collections import Counter
lenA, lenB = [int(x) for x in input().split()]
A = Counter([int(x) for x in input().split()])
B = Counter([int(x) for x in input().split()])
result = []
for i in A:
    if i in B:
        lens = min(A[i], B[i])
        result.extend([i] * lens)
print(len(result)        )
print(*result)
        

    
  
    
    
    
