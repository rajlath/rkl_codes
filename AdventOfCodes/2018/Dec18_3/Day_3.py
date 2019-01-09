# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 07:30:12 2018

@author: rinfo
"""
import re
input = open("input.txt")
data = input.readlines()
data = [x.strip() for x in data]
lists = []
maxw = -1
maxh = -1
for line in data:
    id, left, top, width, height =  map(int, re.findall(r'\d+', line))   
    lists.append([left, top, width, height])
    
matrix = [[0 for x in range(1000)] for y in range(1000)]
for line in lists:
    left = line[0]
    tops = line[1]
    wide = line[2]
    hite = line[3]
    for i in range(wide):
        for j in range(hite):
            matrix[left+i][tops+j] += 1
area = 0            
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        area += matrix[i][j] > 1
print(area)        
        
            
    
  
                                                        

                       
                            
    


