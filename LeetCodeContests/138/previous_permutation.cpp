class Solution:
    def prevPermOpt1(self, A):
        lens = len(A)
        mins = lens - 1
        for i in range(lens - 1, -1, -1):
            if A[i] < A[mins]: mins = i
            if A[i] > A[mins]:
                j = i
                for k in range(lens - 1, -1, -1):
                    if A[k] < A[j]:
                        A[k], A[j] = A[j], A[k]
                        return A
        return A

print(Solution().prevPermOpt1([3, 1, 1, 3]))