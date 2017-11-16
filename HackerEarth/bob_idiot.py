'''
1
W H
WelloHorld
'''

from string import ascii_uppercase as uc, ascii_lowercase as lc

valids = uc + " " + lc
ords   = [ord(x) for x in valids]

for _ in range(int(input())):
    a, b = [x for x in input().split()]
    
    x, y = ords[a], ords[b]
    valids[x], valids[y] = valids[y], valids[x]
    ords[a], ords[b] = y, x
    
mapping = {}
for i, v in enumerate(valids):
    mapping[chr(i)] = chr(v) 
    
print(mapping, valids, ords)       
 

