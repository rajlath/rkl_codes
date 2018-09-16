class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        has = ''
        for i in words:
            for j in rows:
                if i[0].lower() in j:
                    has = j
                    break
            for k in i[1:]:
                if k.lower() not in has:
                    has = ''
                    break
            if has != '':
                ans.append(i)
        return ans

print(Solution().findWords(["asdfghjkl","qwertyuiop","zxcvbnm"]))
