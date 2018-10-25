
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        zeros = S.count("0")
        ans   = 10000000000
        ones  = 0
        for i in range(len(S)):
            ans = min(ans, zeros + ones)
            if S[i] == "0":zeros -= 1
            else:ones += 1
        return min(ans, zeros + ones)


print(Solution().minFlipsMonoIncr("01111"))





