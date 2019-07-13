class Solution(object):
    def sumOfDigits(self, A):
        mins = min(A)
        sums = sum(map(int, str(mins)))
        return 1 - sums % 2

print(Solution().sumOfDigits())        
