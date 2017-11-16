'''
def divs(n, m):
    if m == 1: return [1]
    if n % m == 0: return [m] + divs(n, m - 1)
    return divs(n, m - 1)
def divisorGenerator(n):
    for x in reversed(divs(n, n)):
        print(x)
divisorGenerator(1234)

import math
from functools import reduce
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
    
           
                

buildings = {}
nosOfBldg = int(input())
for i in range(nosOfBldg):
    curr = int(input())
    buildings[i]= factors(curr)
  
     
for _ in range(nosOfBldg):
    curr = int(input())
    cnt = 0
    for k, v in buildings.items():          
        if curr in v: cnt+=1
    print(cnt) 
exit()  

            
'''
cache = {}
max_height = 1
building_heights = {}
nos_of_building  = int(input())
for i in range(nos_of_building):
    curr = int(input())
    max_height= max(curr, max_height)
    building_heights[curr] = building_heights.get(curr, 0) + 1 
    
       
nos_of_queries = int(input())
for i in range(nos_of_queries):
    curr_qry = int(input())
    curr_cnt = 0
    step_by  = curr_qry
    if curr_qry in cache: 
        print(cache[curr_qry]) 
    else:
        while curr_qry <= max_height:
            if curr_qry in building_heights:
                curr_cnt += building_heights[curr_qry]            
            curr_qry+=step_by   
        print(curr_cnt)
        cache[step_by] = curr_cnt 
         
    
'''
n=int(raw_input())
 
# ce=0
maxi=-1
freq={}
table={}
for i in range(n):
    x=int(raw_input())
    if(x>maxi):
        maxi=x
    if(x not in freq):
        freq[x]=1
    else:
        freq[x]+=1
    
    
q=int(raw_input())
for i in range(q):
    count =0
    q1=int(raw_input())
    temp=q1
    if(q1 not in table):
        
        while(q1<=maxi):
            if(q1 in freq):
                count+=freq[q1]
            
            q1=q1+temp
        table[temp]=count
        print count
    else:
        print table[q1]
         
'''        
                
    
     
    
    

    
