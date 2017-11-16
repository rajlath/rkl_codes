'''
3 3 1
1000 2 1 2
1000 2 2 3
3000 3 1 2 3

SAMPLE OUTPUT 
2
1 2 
'''
from collections import defaultdict
junction = []
resident_route = []
nos_junction, nos_possible_lines, nos_resident = [int(x) for x in input().split()]
for _ in range(nos_possible_lines):
    junction[i]  = [int(x) for x in input().split()]    
for _ in range(nos_resident)    :
    resident_route.append([int(x) for x in input().split()])
print(junction, resident_route )    
    
    

 
