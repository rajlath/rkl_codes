'''
SAMPLE INPUT 
agcdgcaag
5
2 a
1 c
1 d
3 g
2 a

SAMPLE OUTPUT 
aggc
'''
from collections import defaultdict
from sys import stdin

lst = defaultdict(list)
ins = stdin.readline().strip()
ins1 = ins
for i,v in enumerate(ins):
    lst[v].append(i)
indx = []
indx = [False] * len(ins)
for _ in range(int(stdin.readline().strip())):
    a = stdin.readline().strip().split()
    ndx, ch = int(a[0]), a[1]        
    pos = lst[ch].pop(ndx-1)
    indx[pos] = True
    
    
ans = []  
for i, v in enumerate(indx)    :
    if not v: 
        ans.append(ins[i])       
        
print("".join(ans))     


