'''
A robot on an infinite grid starts at point (0, 0) and faces north.
The robot can receive one of three possible types of commands:
-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.
The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
If the robot would try to move onto them, the robot stays on the previous grid square
instead (but still continues following the rest of the route.)
Return the square of the maximum Euclidean distance that the robot will be from the origin.

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
'''
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x, y = 0, 0
        obs = set([])
        for ox, oy in obstacles:obs.add((ox, oy))
        mxd = 0
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        curdir = 0
        for c in commands:
            while c > 0:
                nx, ny = x + dirs[curdir][0], y + dirs[curdir][1]
                if (nx, ny) in obs:
                    c = 0
                else:
                    x, y = nx, ny
                    c -= 1
            mxd = max(mxd, x**2 + y**2)
            if c == -2:
                curdir = (curdir + 1) % 4
            elif c == -1:
                curdir = (curdir + 3) % 4
        return mxd

#official
class Solution1(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans

print(Solution().robotSim([4,-1,3], []))
print(Solution1().robotSim([4,-1,3], []))


