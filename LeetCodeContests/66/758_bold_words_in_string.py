
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        isbold = [False] * len(S)

        words = set(words)
        for i in range(1, len(S)+1):
            for j in range(max(0, i-11), i):
                if S[j:i] in words:
                    for k in range(j, i):
                        isbold[k] = True
                    break
        rstr = ""
        lastbold = False
        for i,b in enumerate(isbold):
            if lastbold != b:
                if b:
                    rstr += "<b>"
                else:
                    rstr += "</b>"
                lastbold = b
            rstr += S[i]
        if lastbold:
            rstr += "</b>"
        return rstr

#words = ["ab", "bc"] and S = "aabcd"
sol = Solution()
print(sol.boldWords(["ab", "bc"], "aabcd"))
