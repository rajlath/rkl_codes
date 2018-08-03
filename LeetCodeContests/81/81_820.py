'''
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
'''
class Solution(object):
    def minimumLengthEncoding(self, words):
        seen = set()
        res = 0
        for word in sorted(words, key=lambda w: -len(w)):
            if word in seen: continue
            for i in range(len(word)):
                seen.add(word[i:])
            res += len(word) + 1
        return res

sol = Solution()
print(sol.minimumLengthEncoding(["time", "me", "bell"]))