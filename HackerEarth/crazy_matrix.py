def dfs(matrix, i, j, flag,size, visited):
    if i < 0 or j < 0 or i >=size or j >= size:
        return False
    if matrix[i][j] != flag or visited[i][j]:
        return False
    if i == size -1 and  flag == 1:return True
    if j == size -1 and  flag == 2:return True
    visited[i][j] = True
    if (dfs(matrix, i-1, j-1, flag, size, visited)): return True
    if (dfs(matrix, i, j-1, flag, size, visited))  : return True
    if(dfs(matrix, i+1, j-1, flag, size, visited)) :return True
    if(dfs(matrix, i+1, j, flag, size, visited)) :return True
    if(dfs(matrix, i+1, j+1, flag, size, visited)): return True
    if(dfs(matrix, i, j+1, flag, size, visited)) :return True
    if(dfs(matrix, i-1, j+1, flag, size, visited)):return True
    return False



size = int(input())
matrix = []
for i in range(size):
    matrix.append([int(x) for x in input().split()])

flag1, flag2 = False, False
for j in range(size-1):
    if matrix[0][j] == 1:
        visited = [[0 for _ in range(size)] for _ in range(size)]
        flag1 = dfs(matrix, 0, j, 1, size, visited)
        if flag1:break
for i in range(size-1):
    if matrix[i][0] == 2:
        visited = [[0 for _ in range(size)] for _ in range(size)]
        flag2 = dfs(matrix, i, 0, 2, size, visited)
        if flag2:break


if flag1 and flag2:print("AMBIGUOUS")
elif flag1:print("1")
elif flag2:print("2")
else:print("0")
