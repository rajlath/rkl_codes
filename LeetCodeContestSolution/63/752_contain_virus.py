'''
749. Contain Virus My SubmissionsBack to Contest

Difficulty: Hard
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.
The world is modeled as a 2-D array of cells, where 0 represents uninfected cells, and 1 represents cells contaminated with the virus.
A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.
Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited.
Each day, you can install walls around only one region -- the affected area (continuous block of infected cells) that threatens the most
uninfected cells the following night. There will never be a tie.
Can you save the day? If so, what is the number of walls required? If not, and the world becomes fully infected,
return the number of walls used.

Example 1:
Input: grid =
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
Output: 10
Explanation:
There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

[[0,1,0,0,0,0,1,1],
 [0,1,0,0,0,0,1,1],
 [0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,1]]

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
Example 2:
Input: grid =
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.
Example 3:
Input: grid =
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.
Note:
The number of rows and columns of grid will each be in the range [1, 50].
Each grid[i][j] will be either 0 or 1.
Throughout the described process, there is always a contiguous viral region that will infect strictly more uncontaminated squares in the next round.
'''
class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = 0

        while(True):
            visited = []
            for i in range(m):
                visited.append([0]*n)
            _loc = {}
            c = []
            w = []
            _n = []
            for i in range(m):
                for j in range(n):
                    if(grid[i][j] == 1 and visited[i][j] == 0):
                        visited[i][j] = 1
                        stack = [(i,j)]

                        neig = set([])
                        cand = [(i,j)]
                        wall = 0
                        while(stack):
                            newi,newj = stack.pop()
                            if(newi+1 < m):
                                if(grid[newi+1][newj] == 0):
                                    wall += 1
                                    neig.add((newi+1,newj))

                                if(grid[newi+1][newj] == 1):
                                    cand.append((newi+1,newj))
                                    if(visited[newi+1][newj] == 0):
                                        visited[newi+1][newj] = 1
                                        stack.append((newi+1,newj))

                            if(newi-1 >= 0):
                                if(grid[newi-1][newj] == 0):
                                    wall += 1
                                    neig.add((newi-1,newj))

                                if(grid[newi-1][newj] == 1):
                                    cand.append((newi-1,newj))
                                    if(visited[newi-1][newj] == 0):
                                        visited[newi-1][newj] = 1
                                        stack.append((newi-1,newj))

                            if(newj+1 < n):
                                if(grid[newi][newj+1] == 0):
                                    wall += 1
                                    neig.add((newi,newj+1))

                                if(grid[newi][newj+1] == 1):
                                    cand.append((newi,newj+1))
                                    if(visited[newi][newj+1] == 0):

                                        visited[newi][newj+1] = 1
                                        stack.append((newi,newj+1))

                            if(newj-1 >=0):
                                if(grid[newi][newj-1] == 0):
                                    wall += 1
                                    neig.add((newi,newj-1))
                                if(grid[newi][newj-1] == 1):
                                    cand.append((newi,newj-1))
                                    if(visited[newi][newj-1] == 0):
                                        visited[newi][newj-1] = 1
                                        stack.append((newi,newj-1))

                        total = len(_loc.keys())
                        _loc[total] = cand
                        c.append(len(neig))
                        w.append(wall)
                        _n.append(neig)
            if(not c):
                break
            max_index = 0
            _max = -float('inf')
            for i in range(len(c)):
                if(c[i] > _max):
                    _max = c[i]
                    max_index = i
            for x in _loc[max_index]:
                grid[x[0]][x[1]] = 2
            res += w[max_index]
            for i in range(len(c)):
                if(i == max_index):
                    continue
                for x in _n[i]:
                    grid[x[0]][x[1]] = 1
            #print grid

        return res