def is_safe(board, i, col):
    if any(board[i][y]==True for y in range(col)):
        return False
    x = i
    y = col
    while (x>=0 and y>=0):
        if board[x][y]:return False
        x -= 1
        y -= 1
        
    x = i
    y = col
    while (y >= 0 and x < len(board)):
        if board[x][y]:return False
        x += 1
        y -= 1 
    return True
    
def print_board(board):
    for i in range(len(board[0])):
        print(" ".join(map(str, board[i])))
        
        

def solve_nq(board, col):
    if col > len(board[0]):return True
    
    for i in range(len(board[0])):
        if is_safe(board, i, col):
            board[i][col] = 1
        if solve_nq(board,col+1):
            return True
        else:
            board[i][col] = 0 
    return False              
    

def solve(n):
    board = [[0 for x in range(n)] for y in range(n)]
    if solve_nq(board, 0) == False:
        print("Not possible")
    else:        
        print_board(board) 
        
solve(4)        
        
           
    
