from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.sub(r'[^\w\s]','',paragraph)
        valids = [x.lower() for x in paragraph.split() if x.lower() not in banned]
        return Counter(valids).most_common()[0][0]