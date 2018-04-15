'''
695. Max Area of Island

User Accepted: 1446
User Tried: 1625
Total Accepted: 1462
Total Submissions: 2797

Difficulty: Easy
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0

        def dfs(i, j,m, n,  grid, visited):

            visited[i][j] = True
            area = 1
            dirs = [(-1, 0), (1, 0), (0, -1),(0, 1)]
            for d in dirs:
                x, y = i + d[0], j + d[1]

                if 0<= x < m and 0<= y < n and grid[x][y] and not visited[x][y]:
                    area += dfs(x, y,m, n, grid, visited)
            return area

        m = len(grid)
        n = len(grid[0])
        visited =[[False for _ in range(n)] for _ in range(m)]
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    max_area = max(max_area, dfs(i, j, m, n, grid, visited))

        return max_area










