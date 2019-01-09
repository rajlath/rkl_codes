# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:22:05 2018
coded by : rinfo
"""

stack = []
ins = input()
for i in ins:
    if i.isdigit():
        stack.append(int(i))
    else:
        op1, op2 = stack.pop(), stack.pop()
        if i == "+":
            stack.append(op1 + op2)
        else:
            stack.append(op1 * op2)
print(stack[-1])            
    
   
    
    
        
        
    
            
            
    