r, c = [int(x) for x in input().split()]
matrix = []
for i in range(r):
    matrix.append([int(x) for x in input().split()])
score = [[[0,0] for _ in range(c)] for _ in range(r)]

for i in range(r):
    curr = min(matrix[i])
    for j in range(c):
        score[i][j][0] = curr
cols = list(zip(*matrix))
for i in range(c):
    curr = max(cols[i])
    #print(curr)
    for j in range(r):
        score[j][i][1] = curr
answer = "GUESS"
for i in range(r):
    for j in range(c):
        if score[i][j][0] == score[i][j][1]:
            answer = score[i][j][0]
            break
    if answer != "GUESS":break
print(answer)
