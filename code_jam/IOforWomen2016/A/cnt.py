class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        arr = [x for x in range(1, n+1)]

        cnts = 0
        for i in range(len(arr)):
            cnts += sum([1 for x in str(arr[i]) if x == str(k)])
        return cnts

sol = Solution()
print(sol.digitCounts(19, 0))