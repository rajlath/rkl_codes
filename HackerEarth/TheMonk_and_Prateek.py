'''
2
40 50
SAMPLE OUTPUT 
55 0
Note-1: If all the values of the function are unique, print the maximum value which occurs in the list of the hashed values.
Note-2: If there are multiple hashed values which occur the maximum number of times, print the smallest hashed value with the maximum count.
find out the following information about this list:

The value of the r3gz3n function which occurs the maximum number of times.
Number of collisions with the hash function.
'''
from collections import defaultdict
def r3gz3n(n) :
    sums = sum([int(x) for x in n])
    return int(n) ^ sums
cnts = {}
noe = int(input())
arr = [x for x in input().split()] 
for v in arr:
    key = r3gz3n(v)
    cnts[key] =  cnts.get(key, 0) + 1
cnts = sorted(cnts.items(), key = lambda item:(item[1],item[0]), reverse=True) 
if set(cnts.values())==1:
    print(cnts[0][0], cnts[0][1])
    
start = cnts[0][1] 
smallest = cnts[0][0]  
cn = 0 
for k, v in cnts:
    if v == start:
        smallest = min(smallest, k)
        cn += 1
    else:
        break
        
if cn > 1:
    ans = cnts[smallest]        
            
    
    
        


   
    
    

    
    
    
