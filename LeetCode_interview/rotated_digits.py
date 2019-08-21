class Solution:
    def rotatedDigits(self, N: int) -> int:
        counts = 0
        for i in range(1, N+1):
            sets = set([x for x in str(i)])
            if all(x in ["2","5","6","9"] for x in sets):
                counts += 1
        return counts

print(Solution().rotatedDigits(10))