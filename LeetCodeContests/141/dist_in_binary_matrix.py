from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1:
            return -1
        N = len(grid)
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, -1, -1, -1, 0, 1, 1, 1]
        que = deque([(0, 0)])
        dist = [[-1]*N for i in range(N)]
        dist[0][0] = 1
        while que:
            x, y = que.popleft()
            d = dist[y][x]
            for x0, y0 in zip(dx, dy):
                nx = x + x0; ny = y + y0
                if not 0 <= nx < N or not 0 <= ny < N or grid[ny][nx] == 1:
                    continue
                if dist[ny][nx] != -1:
                    continue
                dist[ny][nx] = d + 1
                que.append((nx, ny))
        return dist[-1][-1]

print(Solution().shortestPathBinaryMatrix( [[0,0,0],[1,1,0],[1,1,0]] ))
