from itertools import groupby
class Solution:
    def normalize(self, s):
        wg = [list(g) for k, g in groupby(s)]
        valids = ""
        for i in wg:
            if len(i)<=2:
                valids += "".join(i)
            else:
                valids += i[0]+i[0]
        return valids

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        wg = self.normalize(S)

        count = 0
        for i in words:
            if self.normalize(i) == wg:count+=1
        return count



#"zzzzzyyyyy"
#["zzyy","zy","zyy"]


sol = Solution()
print(sol.expressiveWords("zzzzzyyyyy",["zzyy","zy","zyy"]))


