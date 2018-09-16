'''
from collections import defaultdict
class Solution(object):
    def dfs(self, u, vis, adj):
        for v in adj:
            if vis[v] and vis[v] is not -vis[u] :
                return True
            else:
                vis[v] = -vis[u]
                dfs(v)
        return False

    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)
        for i in range(len(dislikes)):
            a, b = dislikes[i][0], dislikes[i][1]
            a-= 1
            b-= 1
            adj[a] = b
            adj[b] = a
        visited = [0]*(N+1)
        for i in visited:
            if visited[i]:continue
            visited[i] = 1
            if self.dfs(i, visited, adj):return False
        return True


'''

class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        vis = [0 for x in range(N+2)]
        mark = vis.copy()
        g  =  [[] for x in range(N+2)]
        for x in dislikes:
            a,b = x
            g[a].append(b)
            g[b].append(a)

        for i in range(1,N+1) :
            if vis[i]: continue
            dfs = [i]
            mark[i] = 1
            head = 0
            while head <len(dfs):
                now = dfs[head]
                head+=1
                for x in g[now]:
                    if mark[x] == mark[now]: return False
                    if vis[x]:continue
                    vis[x] = 1
                    mark[x] = 3- mark[now]
                    dfs.append(x)
        return True
print(Solution().possibleBipartition(4, [[1,2],[1,3],[2,4]]))





