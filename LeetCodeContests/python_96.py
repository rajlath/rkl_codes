class Solution:
    def uniquePathsIII(self, grid):
        ways = 0
        begin= None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:begin = [i, j]

        def dfs(row, col, count):
            if row < 0 and row >= len(grid) or col < 0 and col >= len(grid) or grid[row][col] == -1:
                return 0
            elif grid[row][col] == 2: return count == ways + 1
            else:
                ans = dfs(row+1, col, count) + dfs(row-1, col, count) + dfs(row, col+1, count) + dfs(row, col - 1, count)
                grid[row][col] = 0
                return ans
        return dfs(begin[0], begin[1], 0)
print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))


