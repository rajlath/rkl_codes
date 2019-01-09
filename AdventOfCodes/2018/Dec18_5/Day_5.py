# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 07:30:12 2018

@author: rinfo
"""
import re

def reducing(s):
    stack=[" "]
    for i in s:
        if abs(ord(stack[-1]) - ord(i)) == 32:
            stack.pop()
        else:
            stack.append(i)
    return len(stack) - 1

        
input = open("input.txt")
data = input.readline().strip()
alpha = set(data.lower())
mins = 1000000000
for i in alpha:
    curr = data.replace(i, "").replace(i.upper(), "")    
    mins = min(reducing(curr), mins)
print(mins)    




print(reducing(data))
   

        
            
    
  
                                                        

                       
                            
    


