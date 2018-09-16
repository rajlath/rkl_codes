n, m = [int(x) for x in input().split()]
a = []
for _ in range(n):
    a.append(list(str(input())))

visited = [[0 for i in range(m)] for j in range(n)]

ans = []
for i in range(n):
    for j in range(m):
        if a[i][j]=='*':
            x = 1
            while 1:
                if i + x < n and j + x < m and i - x > -1 and j - x > -1:
                    if a[i+x][j]=='*' and a[i-x][j]=='*' and a[i][j+x]=='*' and a[i][j-x]=='*':
                        visited[i][j+x] = 1
                        visited[i][j-x] = 1
                        visited[i-x][j] = 1
                        visited[i+x][j] = 1
                        visited[i][j] = 1
                        x += 1
                    else:
                        break
                else:
                    break
            if x>1:
                ans.append([i, j, x-1])

for i in range(n):
    for j in range(m):
        if a[i][j]=='*' and visited[i][j] == 0:
            print( -1)
            exit(0)

print( len(ans))
for i in ans:
    for j in i[:-1]:
        print( j+1,end=" ")
    print (i[-1], end=" ")
    print()