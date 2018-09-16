'''
Move the Bishop
Time limit: 1000 ms
Memory limit: 128 MB

On a chessboard of size 8 \times 88×8 there is a bishop on cell (R_1, C_1)(R
​1
​​ ,C
​1
​​ ). You want to move the bishop to cell (R_2, C_2)(R
​2
​​ ,C
​2
​​ ), using the minimum number of moves.

A bishop is a chess piece which has no restrictions in distance for each move, but is limited to diagonal movement. Basically, in a move you can take the bishop to any cell that shares a diagonal with the initial cell.

Standard input
The first line contains 44 integers R_1, C_1, R_2, C_2R
​1
​​ ,C
​1
​​ ,R
​2
​​ ,C
​2
​​ .

Standard output
If there is no solution output -1−1.

Otherwise, print the minimum number of moves on the first line.

Constraints and notes
1 \leq R_1, C_1, R_2, C_2 \leq 81≤R
​1
​​ ,C
​1
​​ ,R
​2
​​ ,C
​2
​​ ≤8
Input	Output	Explanation
3 2 6 5
1
The start position is labeled with S

The finish one with F

The path from S to F with #



3 2 3 8
2


3 2 4 4
-1
There's no path from the start position the finish one.

'''
inf = 100
min_dist = [[0 for x in range(10)] for y in range(10)]
dx = [1,  1, -1, -1]
dy = [-1, 1, -1,  1]

def main():
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    for i in range(9):
        for j in range(9):
            min_dist[i][j] = inf

    que = []
    que.append((x1, y1))
    min_dist[x1][y1] = 0
    while que:
        curr = que.pop()
        x, y = curr[0], curr[1]
        c = min_dist[x][y] + 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not 1 <= nx and nx <= 8 and 1 <= ny and ny <= 8:continue
            if min_dist[nx][ny] == inf:
                min_dist[nx][ny] = c
                que = [(nx, ny)] + que
    fcost = min_dist[x2][y2]
    print( -1 if fcost == inf else fcost)


main()







