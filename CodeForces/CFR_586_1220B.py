rows = int(input())
table = [[int(x) for x in input().split()] for _ in range(rows)]
a, b, c = table[0][1], table[0][2], table[1][2]
ans = []
ans.append( int((a * b / c)  ** 0.5))
for i in range(1, rows):
    ans.append(table[0][i] // ans[0])
print(*ans)

