from collections import defaultdict
nodes, edges = [int(x) for x in input().split()]
connections = defaultdict(list)
for _ in range(edges):
    x, y = [int(x) for x in input().split()]
    connections[x].append(y)
    connections[y].append(x)
print(connections)    
query = int(input())    
for _ in range(query):
    a, b = [int(x) for x in input().split()]
    if b in connections[a]:
        print("Yes")
    else:
        print("No")

