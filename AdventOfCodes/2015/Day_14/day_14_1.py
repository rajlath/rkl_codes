import re
from itertools import islice, cycle
nums = re.compile(r'\d+')

def get_cycles(line):
    speed, flied, rested = [int(x) for x in nums.findall(line)]
    return cycle([speed] * flied + [0] * rested)

with open("input.txt") as f:
    reindeer = [ get_cycles(line) for line in f ]
    
    
time = 2503

# Sum up the distance travelled per reindeer up to the given time
sums = [sum(islice(r, time)) for r in reindeer]
print(sums)
print(max(sums))

        
       
        
