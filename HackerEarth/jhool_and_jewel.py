'''
2
rrrruubbbyy
rubrubrubrubrubrubrubrubrubrubrubrubrubrb
'''
from collections import Counter
for _ in range(int(input())):
    s = Counter(list(input()))
    
    cnts = {}
    for x in s:
        if x in "ruby":
            cnts[x] = s[x]
    if len(cnts) == 4:
        print(min(cnts.values()))
    else:
        print(0)    
            
       
        
