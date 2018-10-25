class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_arr, min_arr = A[:], A[:]
        for i in range(1, len(A)):
            max_arr[i] = max(A[i], max_arr[i-1])
        for i in range(len(A) - 2, -1, -1):
            min_arr[i] = min(A[i], min_arr[i + 1])
        print(max_arr, min_arr)
        res = 0

        for i in range(len(A) - 1):
            mv = max_arr[i]
            nv = min_arr[i + 1]
            if mv <= nv:
                return i + 1
        return res + 1

print(Solution().partitionDisjoint([5,0,3,8,6]))