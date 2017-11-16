#!/bin/python

import sys
from collections import defaultdict

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    graph = defaultdict(list)
    visited = defaultdict(int)
    for a0 in range(m):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        graph[x].append(y)
        graph[y].append(x)
      
    all_components = []
    total_happiness = 0
    roads_removed = 0
    for node in graph:                      
        if visited[node] == 0:
            stack = [node]            
            strong = []
            while(stack):                
                cur_node = stack.pop()
                
                if visited[cur_node] == 0:
                    for v in graph[cur_node]:
                        
                        if visited[v] == 0:
                            stack.append(v)                            
                    strong.append(cur_node)
                else:
                    roads_removed+=1
                    
                visited[cur_node]+=1
                print(visited)
            
            size = len(strong)
            
            if size > 1:
                all_components.append(size)
            total_happiness+= ((size-1)*size)
          
    happiness = sorted(all_components)
    print(roads_removed, happiness)  
    if roads_removed < 2:
        total_happiness -= 2*(happiness[0]-1)
        if roads_removed == 0:
            total_happiness -= 2*(happiness[0]-1-1)
    print(total_happiness)
    
'''    
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
    
#!/bin/python

import sys

def find_n():
    global n, edges
    visited = [False for _ in range(n)]
    groups = []
    loop_c = 0
    for i in range(n):
        if not visited[i]:
            gs = 0
            task = [(i, -1)]
            while True:
                #print task
                if not task:
                    break
                
                cur, last = task.pop()
                if visited[cur]:
                    continue
                visited[cur]=True
                gs+=1
                for e in edges[cur]:
                    if e != last:
                        if not visited[e]:
                            task.append((e, cur))
                        else:
                            loop_c += 1
            groups.append(gs)
    return groups, loop_c
if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    edges = [[] for _ in range(n)]
    for a0 in range(m):
        x, y = raw_input().strip().split(' ')
        x, y = [int(x)-1, int(y)-1]
        edges[x].append(y)
        edges[y].append(x)
    
    
    g, loop_c = find_n()
    #print g, loop_c
    g.sort()
    while loop_c < 2:
        loop_c += 1
        for i in range(len(g)):
            if g[i]>1:
                g[i] -= 1
                break
    result = 0
    for i in range(len(g)):
        if g[i]>0:
            result += (g[i]*(g[i]-1))
    print result
'''    
    
    
    
    
        
