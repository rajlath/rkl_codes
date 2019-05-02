class Solution:
    def numPairsDivisibleBy60(self, time):
        k = 60
        freq = [0] * k

        for i in time:
            freq[i%k] += 1
        ans = 0
        for i in range((k//2) + 1):
            if i == 0:
                ans += (freq[0] * (freq[0] - 1))//2
            elif i == k // 2:
                ans += (freq[i] * (freq[i] - 1))//2
            else:
                ans += (freq[i] * freq[k - i])



        return ans

#solution by wengfeng1027
#
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        memo = collections.Counter()
        res = 0
        for t in time:
            t %= 60
            res += memo[(60-t)%60]
            memo[t] += 1
        return res



print(Solution().numPairsDivisibleBy60([10,15,20]))