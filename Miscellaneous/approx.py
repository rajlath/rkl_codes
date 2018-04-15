directions = ["N", "E", "W","S"]
delta      = [[1,0], [0,1], [-1, 0], [0,-1]]

n, m = [int(x) for x in input().split()]
maze = []
for i in range(n):
    maze.append([int(x) for x in input().split()])
print(maze)
sx = 0
sy = 0
coins = maze[sx][sy]
ans = ""
while sx < n and sy < m:
    print(sx, sy)
    coin = []
    for i in range(4):
        nx = sx + delta[i][0]
        ny = sy + delta[i][1]
        if nx >=0 and nx <n and ny >=0 and ny < m:
            coin.append(maze[nx][ny])
        else:coin.append(0)
    print(coin)
    maxcoin = max(coin)
    indx    = coin.index(maxcoin)
    ans += directions[coin.index(maxcoin)]

    sx += delta[indx][0]
    sy += delta[indx][1]
    print
print(ans)



