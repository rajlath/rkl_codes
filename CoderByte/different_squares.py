def differentSquares(matrix):
    answer = set()
    if len(matrix) <= 1 and len(matrix[0]) <= 1:
        return 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            current = []
            current.append(matrix[i - 1][j - 1])
            current.append(matrix[i - 1][j ])
            current.append(matrix[i ][j - 1])
            current.append(matrix[i][j])
            answer.add("-".join(map(str,current)))
    return len(answer)






print(differentSquares([[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]))
