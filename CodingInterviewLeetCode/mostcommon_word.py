from collections import Counter
import re
import string
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paras = ""
        for i in paragraph:
            if i in string.punctuation:
               paras += " "
            else:paras+=i.lower()
        paras = Counter(paras.split()).most_common()
        print(paras)
        for i in paras:
               if i[0] not in banned:
                   return i[0]



print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))