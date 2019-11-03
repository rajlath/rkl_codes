def CheckVictory(board):
    #check if previous move caused a win on vertical line
    if board[0][0] == board[0][1] == board [0][2]:
        return ["Player 2", "Player 1"][board[0][0] == "X"]
    if board[1][0] == board[1][1] == board [1][2]:
        return ["Player 2", "Player 1"][board[1][0] == "X"]
    if board[2][0] == board[2][1] == board [2][2]:
        return ["Player 2", "Player 1"][board[2][0] == "X"]
    if board[0][0] == board[1][0] == board [2][0]:
        return ["Player 2", "Player 1"][board[0][0] == "X"]
    if board[0][1] == board[1][1] == board [2][1]:
        return ["Player 2", "Player 1"][board[0][1] == "X"]
    if board[0][2] == board[1][2] == board [2][2]:
        return ["Player 2", "Player 1"][board[0][2] == "X"]
    if board[0][0] == board[1][1] == board[2][2]:
        return ["Player 2", "Player 1"][board[0][0] == "X"]
    if board[0][2] == board[1][1] == board[0][2]:
        return ["Player 2", "Player 1"][board[0][2] == "X"]


board = []
for i in range(3):
    board.append([x for x in input().split()])
print(CheckVictory(board))
