'''
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix).
It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:
Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
Note:
words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
'''
from collections import defaultdict
class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        filters = defaultdict(int)
        len_words = len(words)
        for i in range(len_words):
            curr = words[i]
            len_curr = len(curr)
            for j in range(len_curr+1):
                for k in range(len_curr+1):
                    pre = ""
                    suf = ""
                    if j > 0:pre = curr[:j]
                    if k < len_curr:suf = curr[k:]
                    key = pre +";"+suf
                    filters[key] = i





    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        key = prefix+";"+suffix
        if key in self.filters:
            return self.filters[key]
        else:
            return -1



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)