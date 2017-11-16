import sys
import re

def gather_magicals(n): 
    magicals=[]
    for i in range(1, n):
        si = str(i) 
        if len(set(si)) != len(si):
            continue        
        if is_magical(si):
            magicals.append(i)        
    return magicals
    

def is_magical(ns):     
    seen = []   
    lens = len(ns)
    a, b = ns[0], ns[0]
    j = 0
    while b not in seen:
        seen.append(b)
        j = (int(b) + j) % lens
        b = ns[j]                        
    if a == b and len(seen) == lens:
        return True
    else:
        return False
        

    
                            
            

        

cef = open("magic_number.txt", "r")
all_magics=[]
all_magics = gather_magicals(10000)

for lines in cef:
    start, end = [int(x) for x  in lines.strip().split()]
    valids = []
    for i in range(start, end+1):
        if i in all_magics:
            valids.append(i)
    print(" ".join(map(str,valids)) if len(valids)>0 else "-1")          


    
