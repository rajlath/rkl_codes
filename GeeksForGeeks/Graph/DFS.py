from collections import defaultdict

class Graph(object):
    '''
    implementation of graph object
    '''
    def __init__(self):
        ''' constructor '''
        self.Graph = defaultdict(list)

    def add_edges(self, u, v):
        '''
        build graph using edges provided
        type: object     vertices source
        type: object     vertices target
        '''
        self.Graph[u].append(v)
    def dfs_helper(self, v, visited):
        '''
        type object v : vertices
        type list :visited
        '''
        visited[v] = True
        print(v, end=" ")
        for i in self.Graph[v]:
            if visited[i] == False:
                self.dfs_helper(i, visited)

    def DFS(self, v):
        visited = [False] * len(self.Graph)
        self.dfs_helper(v, visited)

g = Graph()
g.add_edges(0, 1)
g.add_edges(0, 2)
g.add_edges(1, 2)
g.add_edges(2, 0)
g.add_edges(2, 3)
g.add_edges(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(0)


