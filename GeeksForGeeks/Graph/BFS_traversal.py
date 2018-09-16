from collections import defaultdict
class Graph(object):
    ''' implementatin of directed Graph object'''
    def __init__(self):
        '''çonstrstuctor for graph object'''
        '''Base is a default dictionary of list'''
        self.graph = defaultdict(list)
    def add_edges(self, u, v):
        '''build graph by adding directed edges to graph'''
        '''Type u object : vertices source
           Type v object : vertices target
        '''
        self.graph[u].append(v)

    def bfs(self, s):
        '''
        Type s object : start vertices from which all other vertices will be connected.
        '''
        visited  = [False] * len(self.graph)
        queue    = []
        '''
        add start to queue and mark s as visited.
        '''
        visited[s] = True
        queue.append(s)

        while queue:
            curr = queue.pop(0)
            print(curr, end=" ")
            for i in self.graph[curr]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


g = Graph()
g.add_edges(0, 1)
g.add_edges(0, 2)
g.add_edges(1, 2)
g.add_edges(2, 0)
g.add_edges(2, 3)
g.add_edges(3, 3)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.bfs(2)







