import sys
from collections import defaultdict

nosOfTown , nosOfRoads = [int(x) for x  in input().strip().split()]

connections = defaultdict(list)
visited     = defaultdict(int)

for _ in range(nosOfRoads):
    x, y = [int(x) for x  in input().strip().split()]
    connections[x].append(y)
    connections[y].append(x)
    
    allcomp   = []
    total_happiness =  0
    roads_removed   =  0
    for nodes in connections:
        if visited[nodes] == 0:
            stack = [nodes]
            strong= []
            while len(stack)>0:
                
                current_node = stack.pop()
                if visited[current_node] == 0:
                    for v in connections[current_node]:
                        if visited[v] == 0:
                            stack.append(v)
                    strong.append(current_node)
                else:
                    roads_removed += 1
                print(current_node, stack, strong)    
                
            size = len(strong)  
            if size > 1:
                allcomp.append(size)
            total_happiness+= ((size-1)*size)
            
happiness = sorted(all_components)
if roads_removed < 2:
   total_happiness -= 2*(happiness[0]-1)
   if roads_removed == 0:
        total_happiness -= 2*(happiness[0]-1-1)
        
print(total_happiness)
                
                    
                            
    
    
    
