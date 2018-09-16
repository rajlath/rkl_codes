'''
nots = int(input())
for _ in range(nots):
    _12, _23, _34, _41, _13 = [int(x) for x in input().split()]
    possible = []
    possible.append(sum([_12, _12, _13,_34]))
    possible.append(sum([_12, _12, _41,_34]))
    possible.append(sum([_13, _13, _12,_12,_41]))
    possible.append(sum([_13, _34, _41,_12]))
    possible.append(sum([_13, _13, _41,_12]))

    possible.append(sum([_12,_12, _41, _34]))
    possible.append(sum([_12, _12,_13, _34]))
    possible.append(sum([_12, _13, _13,_41]))
    possible.append(sum([_12, _41, _41,_13]))

    possible.append(sum([_34, _41, _12]))
    possible.append(sum([_13, _41, _41, _12]))
    possible.append(sum([_13, _12, _12, _41]))
    possible.append(sum([_34, _34, _13, _12]))

    possible.append(sum([_34, _13, _12, _34]))
    possible.append(sum([_41, _13, _13,_12]))
    possible.append(sum([_41, _12, _12,_13]))
    possible.append(sum([_34, _34, _41,_13,_13, _12]))
print(print(possible))
'''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distance = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distance[(from_node, to_node)] = distance


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:break

        nodes.remove(min_node)
        current_weight = visited[min_node]
        #print(graph.distance)
        for edge in graph.edges[min_node]:
            if (min_node, edge) in graph.distance:
                weight = current_weight + graph.distance[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node
    print(path)
    return sum(path.values())#visited, path

nots = int(input())

for _ in range(nots):
    wts  = [int(x) for x in input().split()]
    graph = Graph()
    for i in range(1, 5):graph.add_node(i)
    graph.add_edge(1, 2, wts[0])
    #graph.add_edge(2, 3, wts[1])
    graph.add_edge(3, 4, wts[2])
    graph.add_edge(4, 1, wts[3])
    graph.add_edge(1, 3, wts[4])

    mins = int(10e12)
    for i in [1,3,4]:
        mins = min(mins, dijsktra(graph, i))
    print(mins)









