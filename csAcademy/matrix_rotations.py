def count(a):
    if n is 0:return 0
    if n % 2:
        return pow((n+1)//2, 2) + count(n // 2)
    else:
        return pow(n // 2)      + count(n // 2)

n = int(input())
rows = []
for i in range(n):
    rows.append([int(x) for x in input().split()])

#rows  = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        rows[i][j] |= rows[n - i - 1][n - j - 1]
        rows[i][j] |= rows[n - j - 1][i]
        rows[i][j] |= rows[j][n - i - 1]

for i in range(n)        :
    print(*rows[i])
