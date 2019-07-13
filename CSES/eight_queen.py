global N
N = 8

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1 or board[row][col] == "*":
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[row][i] == 1 or board[row][col] == "*":
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[row][i] == 1 or board[row][col] == "*":
            return False
    return True

def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):
      if is_safe(board, i, col):
          board[i][col] = 1
      if solveNQUtil(board, col + 1) == True:
          return True
      board[i][col] = 0
      
    return False

