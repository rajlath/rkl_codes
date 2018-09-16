'''
Problem

Figure 1. The graph from the dataset
The task is to use breadth-first search to compute single-source shortest distances in an
unweighted directed graph.
Given: A simple directed graph with n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex
1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to −1.
See Figure 1 for visual example from the sample dataset.
Sample Dataset
6 6
4 6
6 5
4 3
3 5
2 1
1 4
Sample Output
0 -1 2 1 3 2



ifile = open("rosalind_bfs.txt", "r")
wfile = open("rosalind_bfs_ans.txt", "w")
nodes, edge = [int(x) for x in ifile.readline().split()]
graph = [[0 for x in range(nodes)] for y in range(nodes)]
i = 2
for line in ifile:
        a, b =[int(x) for x in ifile.readline().split()]
        graph[a-1][b-1] = 1
Q = [0]
D = [-1 for y in range(nodes)]
D[0] = 0
while Q:
    z = Q.pop(0)
    for n in range(nodes):
        if D[n] == -1 and graph[z][n] == 1:
            D[n] = D[z] + 1
            Q.append(n)
print(len(D), file=wfile)
for d in D:
    print(d, end = " ", file = wfile)
'''
from collections import defaultdict
from collections import deque

ifile = open("rosalind_bfs.txt", "r")
wfile = open("rosalind_bfs_ans.txt", "w")

nnode, nedge = [int(x) for x in ifile.readline().split()]
graph = defaultdict(list)

for i in range(nedge):
    u, v = [int(x) for x in ifile.readline().split()]
    graph[u].append(v)
visited = {x:0 for x in range(1, nnode+1)}
distance= {x:-1 for x in range(1, nnode)}
distance[1] = 0

visited[1]  = 1
distance[1] = 0

q = deque()
q.append(1)
while q:
    u = q.popleft()
    for v in graph[u]:
        if visited[v] == 1:continue
        visited[v] = 1
        distance[v] = distance[u] + 1
        q.append(v)
for i in range(1,nnode+1):
    print(distance[i], end=" ", file=wfile)

















