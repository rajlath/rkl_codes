class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        time  = 0
        while True:
            done = False
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] in [0, 1]:continue
                    for x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        i1, j1 = i + x[0], j + x[1]
                        if i1 < 0 or i1 > (rows - 1) or j1 < 0 or j1 > (cols -1) or grid[i][j] == 0: continue
                        if grid[i1][j1] == 1:
                            grid[i1][j1] = 2
                            done = True
            print(grid)
            if done:time += 1
            else:break
        ans = time

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = -1
                    break
        return ans

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
