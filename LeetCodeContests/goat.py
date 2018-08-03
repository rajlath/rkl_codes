class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = [x for x in S.split()]
        a = []
        for i, w in enumerate(s):
            if w[0] in "aeiouAEIOU":
                w = w + "ma" + "a" * (i+1)
            else:
                w = w[1:]+w[0]+ "ma" + "a" * (i+1)
            a.append(w)
        return " ".join(a)

sol = Solution()
print(sol.toGoatLatin("I speak Goat Latin"))
'''
Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
'''