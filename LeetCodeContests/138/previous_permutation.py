class Solution:
    def prevPermOpt1(self, A):
        lens = len(A)
        mins = lens - 1
        while mins > 0 and A[mins] >= A[mins - 1]:
            mins -= 1
        if mins == 0: return A
        j = mins - 1
        while j >= mins and A[j] >= A[mins - 1]:
            j -= 1
        A[mins - 1], A[j] = A[j], A[mins - 1]
        return A


print(Solution().prevPermOpt1([3, 1, 1, 3]))