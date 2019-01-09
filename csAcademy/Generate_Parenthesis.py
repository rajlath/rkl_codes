# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 15:56:32 2018
coded by : rinfo
"""
n = 0
s = ['']* 30

def function(x, sum):
    global n
    global s    
    if sum < 0:return
    remain = n - x
    if sum > remain:return 
    if x == n:        
        print("".join(s))
        return
    s[x] = '('
    function(x + 1, sum + 1)
    s[x] = ')'
    function(x + 1, sum - 1)
    
def generate(N):
    global n
    n = N * 2
    function(0, 0)
    
generate(2)    
    
    
    
