class Solution(object):
    def shortestPathLength(self, graph):
        n = len(graph)
        if n < 2: return 0
        newgraph = [set() for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                newgraph[i].add(j)
                newgraph[j].add(i)
        graph = newgraph

        target = 2 ** n - 1
        dp = [set([1 << i]) for i in range(n)]

        for length in range(2 * n - 2):
            newdp = [set(row) for row in dp]
            for i in range(n):
                for j in graph[i]:
                    for mask in dp[i]:
                        if mask | (1 << j) == target:
                            return length + 1
                        newdp[j].add(mask | (1 << j))
            dp = newdp

