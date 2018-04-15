class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        vue, todo = set(), [tuple(board[0] + board[1])]
        T, step = (1,2,3,4,5,0), 0
        while todo:
            todo2 = []
            for p in todo:
                if p in vue: continue
                if p == T: return step
                vue.add(p)
                i = p.index(0)
                p2 = list(p)
                j = (i - 3) if i > 2 else (i + 3)
                p2[i], p2[i - 3] = p2[i - 3], p2[i]
                todo2.append(tuple(p2))
                if i not in (2, 5):
                    p2 = list(p)
                    p2[i], p2[i + 1] = p2[i + 1], p2[i]
                    todo2.append(tuple(p2))
                if i not in (0, 3):
                    p2 = list(p)
                    p2[i], p2[i - 1] = p2[i - 1], p2[i]
                    todo2.append(tuple(p2))
            step += 1
            todo = todo2
        return -1