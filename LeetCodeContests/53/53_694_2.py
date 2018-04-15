class Solution(object):

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        offset = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        def search(i, j, grid):
            ans = 1
            grid[i][j] = 0
            for k in range(4):
                if (i+offset[k][0]) >= 0 and (i + offset[k][0]) < len(grid) and (j+offset[k][1]  >= 0) and (j + offset[k][1]  < len(grid[0])):
                     if grid[i + offset[k][0]][j + offset[k][1]] == 1:
                         ans += search(i + offset[k][0], j + offset[k][1], grid)
            return ans

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, search(i, j, grid))
        return ans;

sol = Solution()
grd = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(sol.maxAreaOfIsland(grd))