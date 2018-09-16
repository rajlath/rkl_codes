'''
Problem

Figure 1. The graph from the dataset
The task is to use depth-first search to compute the number of connected components in a given undirected graph.

Given: A simple graph with n≤10**3 vertices in the edge list format.

Return: The number of connected components in the graph.



Sample Dataset
12 13
1 2
1 5
5 9
5 10
9 10
3 4
3 7
3 8
4 8
7 11
8 11
11 12
8 12
Sample Output
3
Time limit
'''
from collections import defaultdict


def dfs(u):
    global graph
    global visited
    visited[u] = 1
    for i in graph[u]:
        if visited[i] == 0:
            dfs(i)

ifile = open("rosalind_cc.txt", "r")
wfile = open("rosalind_cc_ans.txt", "w")

#nnode, nedge = [int(x) for x in input().split()]
nnode, nedge = [int(x) for x in ifile.readline().split()]
graph = defaultdict(list)
for _ in range(nedge):
    #u, v = [int(x) for x in input().split()]
    u, v = [int(x) for x in ifile.readline().split()]
    graph[u].append(v)
    graph[v].append(u)
visited= {x:0 for x in range(1, nnode+1)}
connected_component = 0
for v in range(1, nnode+1):
    if visited[v] == 0:
        visited[v] = 1
        dfs(v)
        connected_component += 1

print(connected_component)
#print(connected_component, file=wfile)




