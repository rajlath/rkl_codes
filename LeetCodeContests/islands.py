class Solution(object):
    def dfs(self, i, j, col, grid):
        grid[i][j] = col
        stack = [(i, j)]
        sz = 1
        while stack:
            i, j = stack.pop()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = i + di
                nj = j + dj
                if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]) and grid[ni][nj] == 1:
                    grid[ni][nj] = col
                    sz += 1
                    stack.append((ni, nj))
        return sz

    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        M = len(grid[0])
        col = 1
        mp = {}
        mxsz = 0
        for i in xrange(N):
            for j in xrange(M):
                if grid[i][j] == 1:
                    col += 1
                    mp[col] = self.dfs(i, j, col, grid)
                    mxsz = max(mp[col], mxsz)
        for i in xrange(N):
            for j in xrange(M):
                newset = set([])
                if grid[i][j] == 0:
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni = i + di
                        nj = j + dj
                        if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]) and grid[ni][nj] != 0:
                            newset.add(grid[ni][nj])
                newsize = 1 + sum([mp[s] for s in newset])
                mxsz = max(mxsz, newsize)
        return mxsz



        