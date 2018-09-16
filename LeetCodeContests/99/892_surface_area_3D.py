'''
892. Surface Area of 3D Shapes

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell
(i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
'''
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        alls = 0
        noos = 0
        for i in range(n):
            for j in range(m):
                alls += grid[i][j]
                if (j + 1) < m:
                    noos =  min(grid[i][j], grid[i][j+1])
                if (i + 1) < n:
                    noos =  min(grid[i][j], grid[i+1][j])
                if grid[i][j] > 0:
                    noos += grid[i][j] - 1
        return alls * 6  - noos * 2

print(Solution().surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))

