class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        max_top_bot = [max(row) for row in grid]
        max_lef_rit = [max(row) for row in zip(*grid)]
        #print(max_lef_rit, max_top_bot)
        height_sum = 0
        for c in range(len(grid)):
            for r in range(len(grid)):
                height_sum += min(max_top_bot[r], max_lef_rit[c]) - grid[c][r]
        return height_sum


print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))