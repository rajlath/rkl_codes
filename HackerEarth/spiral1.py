def print_grid(s, n):
    for i in range(n):
        for j in range(n):
            print(s[i][j], end=" ")
    print()


n = int(input())
vec = []
for i in range(n):
    vec.extend([int(x) for x in input().split()])

vec = sorted(vec)
ans = [[0 for x in range(n)] for y in range(n)]
k = 0
c1=0
c2=n-1
r1=0
r2=n-1
done = False
while k <= (n*n):
    for i in range(c1, c2+1):
        if k >= n*n:
            break
        ans[r1][i] = vec[k]
        k+=1
    if k >= n*n:break
    for i in range(r1+1, r2):
        if k >= n*n:
            done=True
            break
        ans[i][c2] = vec[k]
        k+=1

    if k >= n*n:break
    for i in range(c2, c1,-1):
        if k >= n*n:
            done=True
            break
        ans[r2][i] = vec[k]
        k+=1

    if k >= n*n:break
    for i in range(r2, r1, -1):
        if k >= n*n:
            done=True
            break
        ans[i][c1] = vec[k]
        k+=1
    if k >= n*n:break


    c1+=1
    c2-=1
    r1+=1
    r2-=1


for i in range(n):
    for j in range(n):
        print(ans[i][j], end=" ")
    print()
