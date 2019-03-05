class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def findrook():
            for i, row in enumerate(board):
                for j, c in enumerate(row):
                    if c == 'R': return i, j
        def pawns(i, j, di, dj):
            while True:
                i += di
                j += dj
                if 0 <= i < 8 and 0 <= j < 8 and board[i][j] != 'B':
                    if board[i][j] == 'p': return 1
                else: break
            return 0
        i, j = findrook()
        r = 0
        r += pawns(i, j, +1, 0)
        r += pawns(i, j, -1, 0)
        r += pawns(i, j, 0, +1)
        r += pawns(i, j, 0, -1)
        return r


print(Solution().numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))