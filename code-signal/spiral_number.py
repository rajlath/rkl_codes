def spiralNumbers(n):
    res = [[0] * n for k in range(n)]
    r, c = 0, -1
    dr, dc = 0, 1
    for k in range(n * n):
        while True:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and res[nr][nc] == 0:
                break
            dr, dc = -dc, dr
        r, c = nr, nc
        res[r][c] = k + 1
    return res

def spiralNumbers(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m