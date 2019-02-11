
n, m = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            k = dfs(i, j, grid[i][j])
            






