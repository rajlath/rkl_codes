import re
from math import gcd

posdict = {}  
with open("input.txt") as f:
     data = [x.strip() for x in f.readlines()]
for posmov in data[2:]     :
    pos,src,tgt = re.findall(r"[A-Z]+", posmov)    
    posdict[pos] = [src, tgt]
src= [x for x in data[0]]

valids = [key for key in posdict if key.endswith("A")] 

cycles = []
for current in valids:
    cycle = []
    current_src = src
    step_count = 0
    first_z = False

    while True:
        while step_count == 0 or not current.endswith("Z"):
            step_count += 1
            current = posdict[current][0 if current_src[0] == "L" else 1]
            #current = posdict[current][["L", "R"].index(current_src)]
            current_src = current_src[1:] + [current_src[0]]

        cycle.append(step_count)

        if not first_z :
            first_z = current
            step_count = 0
        elif current == first_z:
            break

    cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]

lcm = nums.pop()

for num in nums:
    lcm = lcm * num // gcd(lcm, num)
    
print(lcm)    


  