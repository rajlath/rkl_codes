def can_be_attacked(board, i, j):
    rows = len(board)
    cols = len(board[0])
    for x in range(rows):
        if board[x][j] == 1:return True        
    for x in range(cols):
        if board[i][x] == 1:return True 
    for x in range(rows):
        for y in range(cols):
            if (x, y) == (i, j):continue
            if x+y == i+j and board[x][y]==1: 
                    return True 
            if abs(x-y) == abs(i-j) and board[x][y]==1:
                return True           
            
    return False 
    

    
def queen_positions(board, n):
    if n == 0: return True
    rows = len(board)
    cols = len(board[0])    
    for i in range(rows):
        for j in range(cols):
            if can_be_attacked_1(board, i, j):continue
            board[i][j] = 1
            if queen_positions(board, n-1):return True
            board[i][j]= 0
    
    return False        
            
board = [[0]*4 for i in range(4)]
print(queen_positions(board, 4)) 
print(board)           
            
                
            
                
           
