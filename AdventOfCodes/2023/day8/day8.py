import re

posdict = {}  
with open("input.txt") as f:
     data = [x.strip() for x in f.readlines()]
for posmov in data[2:]     :
    pos,src,tgt = re.findall(r"[A-Z]+", posmov)    
    posdict[pos] = [src, tgt]
cur= [x for x in data[0]] 
  
    
current = "AAA" 
steps = 0   
while current != "ZZZ":
    steps += 1
    curr_mov = cur.pop(0)
    cur.append(curr_mov)
    current = posdict[current][["L", "R"].index(curr_mov)]
print(steps)        
    
 