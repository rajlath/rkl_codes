#  thanks to lbjlc

import collections
class Solution(object):
    def longestStrChain(self, words):

        words = sorted(words, key = lambda x: len(x))
        dp = collections.defaultdict(int)
        res = 0
        for word in words:
            l = len(word)
            for i in range(l):
                tmp = word[:i] + word[i + 1:]
                if tmp in dp:
                    dp[word] = max(dp[word], dp[tmp] + 1)
                else:
                    dp[word] = max(dp[word], 1)
            res = max(res, dp[word])
        return res
