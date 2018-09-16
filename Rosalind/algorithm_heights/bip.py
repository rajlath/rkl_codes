'''
Problem

Figure 1. The graphs from the dataset
A bipartite graph is a graph G=(V,E) whose vertices can be partitioned into two sets (V=V1∪V2 and V1∩V2=∅) such that there are no edges between vertices in
the same set (for instance, if u,v∈V1, then there is no edge between u and v).
There are many other ways to formulate this property. For instance, an undirected graph is bipartite if and only if it can be colored with just two colors.
Another one: an undirected graph is bipartite if and only if it contains no cycles of odd length.
Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.
Given: A positive integer k≤20 and k simple graphs in the edge list format with at most 103 vertices each.
Return: For each graph, output "1" if it is bipartite and "-1" otherwise.
See Figure 1 for visual example from the sample dataset.

Sample Dataset
2

3 3
1 2
3 2
3 1

4 3
1 4
3 1
1 2
Sample Output
-1 1
'''
def DFS(adj, v, visited, departure, time):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            DFS(adj,u, visited, departure, time )
    time += 1
    departure[v] = time
def isDAG(adj, N):
    visited = [0] * N
    departure=[0] * N
    time = 0
    for i in range(N):
        DFS(adj, i, visited, departure, time)
    for u in range(N):
        for v in adj[u]:
            if departure[u] <= departure[v]:
                return False
    return True

from collections import defaultdict
ifile = open("rosalind_bip.txt", "r")
wfile = open("rosalind_bip_ans.txt", "w")
n = int(ifile.readline())
for _ in range(n):
    ifile.readline()
    adj = defaultdict(list)
    nodes, edges = [int(x) for x in ifile.readline().split()]
    #print(nodes, edges)
    visited = [0] * (nodes+1)
    colors  = [0] * (nodes+1)
    for _ in range(edges):
        u, v = [int(x) for x in ifile.readline().split()]
        adj[u].append(v)
    print( 1 if isDAG(adj, nodes) else -1, file=wfile)










