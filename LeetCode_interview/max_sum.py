class Solution:
    def kConcatenationMaxSum(self, arr, k):
        mods = int(10 ** 9 + 7)
        if all(x>0 for x in arr):
            return (sum(arr) * k) % mods
        d = arr * k
        maxsofar = -99999
        maxending = 0
        for i in d:
            maxending = (maxending + i)
            if maxending < 0:
                maxending = 0
            if maxsofar < maxending:
                maxsofar = maxending % mods


        return maxsofar

print(Solution().kConcatenationMaxSum([1,2], 3))