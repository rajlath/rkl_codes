class Solution:
    def largest1BorderedSquare(self, grid):
        height = len(grid)
        width = len(grid[0])
        R = [[0] * 101 for _ in range(101)]
        D = [[0] * 101 for _ in range(101)]
        for y in range(height - 1, -1, -1):
            for x in range(width - 1, -1, -1):
                if grid[y][x]:
                    R[y][x] = R[y][x + 1] + 1
                    D[y][x] = D[y + 1][x] + 1
        ma = 0
        for x in range(width):
            for y in range(height):
                l = 1
                while l <= min(R[y][x], D[y][x]):
                    if R[y+l-1][x]>=l and  D[y][x+l-1]>=l: ma=max(ma,l*l);
                    l += 1
        return ma

print(Solution().largest1BorderedSquare([[1,1,0,0]]))
