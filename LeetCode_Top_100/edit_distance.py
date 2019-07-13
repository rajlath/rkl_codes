class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.cache = {}
        return self.computeLevenshtein(word1, len(word1), word2, len(word2))


    def computeLevenshtein(self, s1, i, s2, j):
        if i <= 0:
            return j

        if j <= 0:
            return i

        s1 = s1[:i]
        s2 = s2[:j]
        if self.cache.get(s1+s2):
            return self.cache[s1+s2]

        if s1[i-1] == s2[j-1]:
            dist = self.computeLevenshtein(s1, i - 1, s2, j - 1)
            self.cache[s1+s2] = dist
            return dist

        else:
            dist = min(
                self.computeLevenshtein(s1, i - 1, s2, j - 1),
                self.computeLevenshtein(s1, i - 1, s2, j),
                self.computeLevenshtein(s1, i, s2, j - 1))
            self.cache[s1+s2] = dist + 1
            return dist + 1
