class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        new_words = [[order.index(char) for char in word] for word in words]
        #print(new_words)
        for i in range(len(new_words)-1):
            if new_words[i] > new_words[i+1]:
                return False
        return True

print(Solution().isAlienSorted(["world","sorld","world"], order = "worldabcefghijkmnpqstuvxyz"))
