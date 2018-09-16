matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
'''
def is_valid(matrix, i, j):
    return 0<= i < len(matrix)-1 and 0 <= j < len(matrix[0]) - 1

def minesweeper(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    ans  = [[0 for x in range(cols)] for y in range(rows)]
    matrix = [[1 if matrix[i][j] else 0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    print(matrix)

    offset = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==1:ans[i][j] = 1
            for a in offset:
                x, y = i + a[0], j + a[1]
                if is_valid(matrix, x, y):
                    ans[i][j] += matrix[x][y] == 1
    return ans
'''
def minesweeper(matrix):
    r = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for a in range(i-1,i+2):
                for b in range(j-1,j+2):
                    try:

                        if a < 0 or b < 0:
                            continue
                        if matrix[i][j]:
                            r[a][b] += 1

                    except IndexError:
                        continue
            if matrix[i][j]: r[i][j] -= 1
    return r

print(minesweeper(matrix))



