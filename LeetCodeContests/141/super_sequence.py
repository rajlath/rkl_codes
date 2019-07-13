class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        m = len(str1)
        n = len(str2)
        dp = [[None for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        res = ''
        k, l = m,n
        while k > 0 and l > 0:
            if str1[k - 1] == str2[b - 1]:
                res = str1[k - 1] + res
                k -= 1
                l -= 1
            elif dp[k - 1][l] < dp[k][l - 1]:
                res = str1[k - 1] + res
                k -= 1
            else:
                res = str2[l - 1] + res
                l -= 1
        while k > 0:
            res = str1[k - 1] + res
            k -= 1
        while l > 0:
            res = str2[l - 1] + res
            l -= 1
        return res




print(Solution().shortestCommonSupersequence(str1 = "abac", str2 = "cab"))
