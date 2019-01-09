from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sc = Counter(s)
        ans= -1
        for i, v in enumerate(s):
            if sc[v] == 1:
                ans = i
                break
        return ans

print(Solution().firstUniqChar("loveleetcode"))