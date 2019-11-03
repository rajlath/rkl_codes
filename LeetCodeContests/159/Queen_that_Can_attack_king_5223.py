class Solution:
    def queensAttacktheKing(self, queens, king):
        kr, kc = king
        can = []
        for i in queens:
            qr, qc = i
            if qr == kr or kc == qc or abs(qr - kr) == abs(qc - kc):
                can.append(i)
        return can

print(Solution().queensAttacktheKing([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [3,3]))