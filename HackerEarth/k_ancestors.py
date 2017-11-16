
'''
5 2
1 1 2 1 2
1 2
1 3
2 4
2 5
'''

from sys import setrecursionlimit
from collections import defaultdict
 
setrecursionlimit(1000000)

def dfs(x):
    visited[x] = True
    nodes[colors[x]].append(x)
    for i in connections[x]:
        if not visited[i]:
            if len(nodes[colors[i]]) > color_cnt:
                ans[i] = nodes[colors[i]][len(nodes[colors[i]]) - color_cnt]
            dfs(i)  
    nodes[colors[x]].pop()          
                
   
    
    
node_cnt, color_cnt = [int(x) for x in input().split()]
colors = [0] + [int(x) for x in input().split()]
connections = defaultdict(list)
visited = [0] * (node_cnt + 1)
#build connection dictionary
for _ in range(node_cnt - 1):
    src, tgt = [int(x) for x in input().split()]
    connections[src].append(tgt)
    connections[tgt].append(src)
    
nodes = defaultdict(list)    
ans   = [-1] * (node_cnt + 1)

dfs(1)
for i in range(1, node_cnt+1): print(ans[i],end=",")
    


 

 


    
 

 

