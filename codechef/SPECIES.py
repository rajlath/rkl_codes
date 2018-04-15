'''
Input:
6
3
..?
.?B
G..
2
GG
..
3
?..
.??
??.
3
??P
???
??B
7
?.?.?.?
.?.?.?.
?.?.?.?
.?.?.?.
?.?.?.?
.?.?.?.
?.?.?.?
2
PP
PP

Output:
1
0
6
0
288603514
1
'''
dx  = [0,0,1,-1]
mod = 1000000007
dy  = [1,-1,0,0]
#vis[57][57];
def issafe(x, y):
    global grid, vis
    if x<0 or x==n or y<0 or y==n or grid[x][y] == '.' or vis[x][y] == 1:
        return False
    return True

def dfs(x, y):
    global tot, vis, cb, cp, cg, q
    tot+=1
    vis[x][y] = 1


    if grid[x][y] == 'B':
        cb+=1
    elif grid[x][y] == 'P':
        cp+=1
    elif grid[x][y] == 'G':
        cg+=1
    elif grid[x][y] == '?':
        q+=1
    for i in range(4):
        if issafe(x+dx[i], y+dy[i]):
            dfs(x+dx[i], y+dy[i])


for _ in range(int(input())):
    n = int(input())
    grid = []
    for i in range(n):
        grid.append([x for x in input()])
    vis = [[0 for x in range(n+5)] for y in range(n+5)]
    ans = 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] != "." and vis[i][j] != 1:
                tmp = 0
                cg  = 0
                tot = 0
                cb  = 0
                cp  = 0
                q  = 0
                dfs(0, 0)
                if tot == 1:
                    if q == 1:
                        tmp += 3
                    else: tmp += 1
                else:
                    if cg > 0 or (cb > 0 and cp > 0):tmp=0
                    else:
                        if q > 0:
                            if cb > 0 or cp > 0 : tmp += 1
                            else: tmp += 2
                        else:
                           tmp += 1
        ans = (ans * tmp) % mod

    print(ans)



