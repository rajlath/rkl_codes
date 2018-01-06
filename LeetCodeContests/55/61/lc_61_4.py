'''
741. Cherry Pickup My SubmissionsBack to Contest

Difficulty: Hard
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells
(cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
'''
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cache = dict()
        point =self.twoPoint(grid, 0, 0, 0, 0, cache)
        return point if point > -1 else 0

    def twoPoint(self, grid, x1, y1, x2, y2, cache):
        m = len(grid)
        n = len(grid[0])

        if x1 >= n or y1 >= m or x2 >= n or y2 >= m or grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return -1

        if x1 == n-1 and y1 == m-1:
            return grid[x1][y1]

        key = tuple(sorted([(x1, y1), (x2, y2)]))
        if key in cache:
            return cache[key]

        ret = -1
        mPoint = -1
        for p1 in [(x1+1,y1), (x1,y1+1)]:
            for p2 in [(x2+1,y2), (x2,y2+1)]:
                point = self.twoPoint(grid, p1[0], p1[1], p2[0],p2[1], cache)
                mPoint = max(mPoint, point)
        if mPoint > -1:
            ret = grid[x1][y1] + grid[x2][y2] + mPoint
            if (x1,y1) == (x2,y2):
                ret -= grid[x1][y1]
        cache[key] = ret
        return ret


 from collections import deque

class Solution(object):
    def solve(self, grid, dp, steps, i1, i2):
        n = len(grid)
        j1 = steps-i1
        j2 = steps-i2
        if steps == 2*(n-1) and i1 == n-1 and i2 == n-1:
            return grid[n-1][n-1]
        if i1 == n or j1 == n or i2 == n or j2 == n or grid[i1][j1] == -1 or grid[i2][j2] == -1:
            return -1000000
        if (steps,i1,i2) in dp:
            return dp[(steps, i1, i2)]
        val = -1000000
        if i1 == i2 and j1 == j2:
            cur = grid[i1][j1]
        else:
            cur = grid[i1][j1] + grid[i2][j2]
        val = max(val, cur + self.solve(grid, dp, steps+1, i1+1, i2))
        val = max(val, cur + self.solve(grid, dp, steps+1, i1, i2+1))
        val = max(val, cur + self.solve(grid, dp, steps+1, i1, i2))
        val = max(val, cur + self.solve(grid, dp, steps+1, i1+1, i2+1))
        dp[(steps, i1, i2)] = val
        return val

