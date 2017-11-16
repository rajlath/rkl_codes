'''
SAMPLE INPUT 
4
G: I want to go on 19
M: No that is not possible lets go on 21
G: No 19 is final and 21 is not
M: OKAY as you wish
SAMPLE OUTPUT 
Date
'''
import re
rc = re.compile(r'\d+')
weights = {}
for i in range(int(input())):
    p, msg = input().split(":")
    dc = rc.findall(msg)
    for i in dc:
        if p == "G":
            weights[i] = weights.get(i, 0) + 2
        else:
            weights[i] = weights.get(i, 0) + 1
max_wt = -1e9
all_max = []
for k, v in weights.items():
    max_wt = max(max_wt, v)    
print(key)        
    
                
        
                
            



