class Solution:
    def missingNumber(self, arr):
        if len(set(arr)) == 1:
            return 0
        n = len(arr)
        a, b = max(arr), min(arr)
        diff = (a - b) // n
        if arr[0] == a:
            for i in range(n-1):
                if arr[i] - diff != arr[i+1]:
                    return arr[i] - diff
        else:
            for i in range(n - 1):
                if arr[i+1 ] - arr[i] != diff:
                    return arr[i] + diff

print(Solution().missingNumber([0,0,0,0]))