from collections import defaultdict
edges = []
cnt = 0

node_cnt, edge_cnt  =  [int(x) for x in input().split()]
edges = []
adj_list = defaultdict(list)
for _ in range(edge_cnt):
    s, e = [int(x) for x in input().split()]
    edges.append( (s, e) )

for s, e in edges:
    adj_list[e].append(s)

def dfs_iter(graph, root):
	visited = []
	stack = [root, ]
	while stack:
		node = stack.pop()
		if node not in visited:
			visited.append(node)
			stack.extend([x for x in graph[node] if x not in visited])
	return visited

b = []
for a in adj_list:
	b.append(a)
for a in b:
	if  len(dfs_iter(adj_list, a)) % 2 == 0:
		cnt += 1

print (cnt-1)