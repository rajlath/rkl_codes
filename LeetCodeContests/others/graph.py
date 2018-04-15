class Solution(object):
    class Graph(object):
        def __init__(self, V):
            self.V = V
            self.graph = [[0 for column in range(V)] for row in range(V)]

        def isBipartite(self, src):
            colorArr = [-1] * self.V
            colorArr[src] = 1
            queue = []
            queue.append(src)
            while queue:
                u = queue.pop()
                if self.graph[u][u] == 1:
                    return False
                for v in range(self.V):
                    if self.graph[u][v] == 1 and colorArr[v] == -1:
                        colorArr[v] = 1 - colorArr[u]
                        queue.append(v)
                    elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                        return False
            return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        g = self.Graph(len(graph))
        g.graph = graph
        return  "Yes" if g.isBipartite(0) else "No"

sol = Solution()
print(sol.isBipartite([[1,3], [0,2], [1,3], [0,2]]))