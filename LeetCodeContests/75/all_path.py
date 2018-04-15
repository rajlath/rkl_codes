class Solution(object):
    def allPathsSourceTarget(self, graph, start = 0):
        if not graph: return []
        if len(graph) == 1: return [[start]]
        res = []
        for y in graph[0]:

            for path in self.allPathsSourceTarget(graph[y-start:], y):
                res.append([start] + path)
        return res

sol = Solution()
print(sol.allPathsSourceTarget([[1,2], [3], [3], []] ))