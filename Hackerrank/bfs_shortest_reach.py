import queue
from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(list)

    def connect(self,x,y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.n)]
        q = queue.Queue()
        distances[root] = 0
        q.put(root)

        while not q.empty():
            node = q.get()
            children = self.edges[node]
            curr_dis = distances[node]
            for child in children:
                if distances[child] == -1:
                    distances[child] = curr_dist + 6
                    q.put(child)
        distances.pop(root)
        print(*distances)

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)

