# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:23:53 2018

@author: rinfo
"""

def give_bin(n):
    arr = []
    for l in range(1,n+1):
        each_m = n//l
        for each in range(1,each_m+1):
            s = ''
            for i in range(l):
                if i%2==1:
                    s += '0'*each
                else:
                    s += '1'*each
            arr.append(s)
    return arr

print(give_bin(6))


