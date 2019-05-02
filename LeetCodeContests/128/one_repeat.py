class Solution(object):
    def numDupDIgitsAtMostN(self, N):
        self.answer = 0

        def DFS(now, s, N):
            if now > N:return
            self.answer += 1
            for i in range(10):
                if not (1 << i) & s:
                    DFS(now * 10 + i, 1 << i | s, N)

        for i in range(10):
            DFS(i, 1 << i, N)
        return N - self.answer

print(Solution().numDupDIgitsAtMostN(20))