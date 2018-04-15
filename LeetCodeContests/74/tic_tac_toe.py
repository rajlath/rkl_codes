class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        first=0
        second=0

        for s in board:
            for i in range(3):
                if s[i]=="X": first+=1
                elif s[i]=="O": second+=1

        if first>5 or second>4: return False
        if first-second>=2: return False
        if first<second: return False

        f=self.check(board, "X")
        s=self.check(board, "O")
        if f==1 and s==1: return False
        if s==1 and first>second: return False
        if f==1 and first==second: return False
        return True

    def check(self, board, char):
        if board[0][0]==char and board[0][1]==char and board[0][2]==char: return 1
        if board[1][0]==char and board[1][1]==char and board[1][2]==char: return 1
        if board[2][0]==char and board[2][1]==char and board[2][2]==char: return 1

        if board[0][0]==char and board[1][0]==char and board[2][0]==char: return 1
        if board[0][1]==char and board[1][1]==char and board[2][1]==char: return 1
        if board[0][2]==char and board[1][2]==char and board[2][2]==char: return 1

        if board[0][0]==char and board[1][1]==char and board[2][2]==char: return 1
        if board[0][2]==char and board[1][1]==char and board[2][0]==char: return 1
        return 0
