def is_safe(grid, visited, x, y):
    if grid[x][y]=="*" or visited[x][y]:
        return False
    return True

def is_valid(grid, x, y):
    m,n = len(grid), len(grid[0])
    return x<m and y < n and x>=0 and y>=0

def find_shorted_path(grid, visited, cx, cy, dx, dy, dist,min_dist):
    if cx == dx and cy == dy:
        min_dist = min(min_dist, dist)
        print('here')
    visited[cx][cy] = 1
    if is_valid(grid, cx+1,cy) and is_safe(grid, visited, cx+1, cy):
        find_shorted_path(grid, visited, cx+1, cy, dx, dy,dist,min_dist)
    if is_valid(grid, cx-1,cy) and is_safe(grid, visited, cx-1, cy):
        find_shorted_path(grid, visited, cx-1, cy, dx, dy,dist,min_dist)
    if is_valid(grid, cx,cy+1) and is_safe(grid, visited, cx, cy+1):
        find_shorted_path(grid, visited, cx, cy+1, dx, dy,dist,min_dist)
    if is_valid(grid, cx,cy-1) and is_safe(grid, visited, cx, cy-1):
        find_shorted_path(grid, visited, cx, cy-1, dx, dy,dist,min_dist)
    visited[cx][cy] = 0







n, m, q = [int(x) for x in input().split()]
grid = []
for i in range(n):
    grid.append([x for x in input().split()])
sx, sy = [int(x) for x in input().split()]
visited = [[0 for x in range(n)] for y in range(m)]
for _ in range(q):
    dx, dy = [int(x) for x in input().split()]
    min_dist = int(10e9)
    find_shorted_path(grid, visited, sx, sy, dx, dy, 0, min_dist)
    print(min_dist)








