class Solution(object):
    def validTicTacToe(self, board):
        FIRST, SECOND = 'XO'
        x_count = sum(row.count(FIRST) for row in board)
        o_count = sum(row.count(SECOND) for row in board)

        def win1(board, c):
            wins= [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
            for i in range(8):
                if board[wins[i][0]] == c and board[wins[i][1]] == c and board[wins[i][2]] == c:
                    return true;
            return False



        def win(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True

            return (player == board[1][1] == board[0][0] == board[2][2] or
                    player == board[1][1] == board[0][2] == board[2][0])

        if o_count not in [x_count-1, x_count]: return False
        if win1(board, FIRST) and x_count-1 != o_count: return False
        if win1(board, SECOND) and x_count != o_count: return False

        return True


sol = Solution()
print(sol.validTicTacToe(["XXX", "   ", "OOO"]))