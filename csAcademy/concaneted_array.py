# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:22:05 2018
coded by : rinfo
"""

import re
zeros = re.compile(r'[0]+')
n, k = [int(x) for x in input().split()]
ins  = input()
pref = 0
suff = 0
lst  = max([len(x) for x in zeros.findall(ins)])
if lst == n:
    print(n * k)
else:
    for i in range(n):
        if ins[i] == "0":
            pref += 1
        else:
            break
    for i in range(n-1, -1, -1):
        if ins[i] == "0":
            suff += 1
        else:
            break
        
print(lst, pref, suff)            
if k > 1:
    print(max(lst, pref + suff))
else:
    print(lst)    
        