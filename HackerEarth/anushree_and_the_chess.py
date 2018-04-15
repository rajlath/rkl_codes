'''
SAMPLE INPUT
1
8 1 1
SAMPLE OUTPUT
100.00
'''

for _ in range(int(input())):
    n, x, y = [int(x) for x in input().split()]
    board = [[0 for x  in range(n)] for y in range(n)]
    visited = [[0 for x  in range(n+1)] for y in range(n+1)]
    dx = [ 2, 1, -1, -2, -2, -1,  1,  2 , 2]
    dy = [ 1, 2,  2,  1, -1, -2, -2, -1 , 1]
    visited[x][y] =  1
    moves = 1
    q = []
    q.append([x, y])
    while len(q)> 0:
        curr = q.pop()
        x1 , y1 = curr[0], curr[1]
        for k in range(8):
            nx = x1 + dx[k]
            ny = y1 + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            else:
                if  visited[nx][ny]==0:
                    moves += 1
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    print(moves)
    ans = ((n * n ) / moves) * 100
    print(visited)
    print("{0:.2f}".format(ans))

