from collections import defaultdict
nodes = 0
def dfs(n):
    global adj, done, nodes
    nodes += 1
    done[n] = True
    for i in adj:
        if not done[i]:
            dfs(i)
   

for _ in range(int(input())):
    adj = defaultdict(list)    
    n, m, cl, cr = [int(x) for x in input().split()]
    done=[0] * n
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        adj[a].append(b)
        adj[b].append(a)
        
        cost = 0
        for i in range(n):
            if not done[i]:
                nodes = 0
                dfs(i)
                cost += cl
                if cl > cr:
                    cost+=(cl*(nodes-1))
                else:
                    cost+=(cr*(nodes-1))
    print(cost)        
                
        
       
    
    
