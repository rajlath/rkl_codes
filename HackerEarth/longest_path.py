'''
6 2
4 2 3 2 3 5
1 2
1 3
2 4
2 5
3 6
'''
from collections import defaultdict
def DFS(arr,k, G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]
    seen.append(v)
    paths = []
    for t in G[v]:
        #if t not in seen and arr[v-1]%k==0:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(arr, k, G, t, seen[:], t_path))
    return paths

nodes, divs = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
graph = defaultdict(list)
for i in range(nodes-1):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
paths = DFS(arr, divs, graph, 1)
longest = int(-10e9)
#print(paths)
for x in paths:
    if all(y%divs==0 for y in x[1:]):
        print(x)
        longest = max(longest, len(x))
print(longest-1)
