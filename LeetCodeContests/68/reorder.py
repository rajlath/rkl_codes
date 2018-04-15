from collections import Counter
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = Counter(S)
        cnts  = []
        for c in count:
            cnts.append((count[c], c))
        if cnts[0][0] > (len(S) + 1)/2 :
            return ""
        result = ["" for i in range(len(S))]
        i = 0
        for num,c in cnts:
            for _ in range(num):
                result[i] = c
                i += 2
                if i >= len(S):
                    i = 1
        return "".join(result)

sol = Solution()
print(sol.reorganizeString("aab"))