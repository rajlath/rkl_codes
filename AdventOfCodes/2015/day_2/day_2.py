# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 20:11:46 2018

@author: rinfo
"""
def calc(x):
    a, b, c = x
    a1 = a * b
    a2 = a * c
    a3 = b * c
    return min(a1, a2, a3) + (2 * a1 + 2 * a2 + 2 * a3)

def calc2(x):
    a, b, c = x
    m1, m2 = sorted([a,b,c])[:2]
    return 2*m1 + 2 * m2 + (a * b * c)

dims = [[int(x) for x in y.split("x")] for y in open("input.txt").readlines()]
needed = 0
ribbon = 0
for x in dims:    
    needed += calc(x)
    ribbon += calc2(x)
    
print(needed)    
print(ribbon)
    
    
