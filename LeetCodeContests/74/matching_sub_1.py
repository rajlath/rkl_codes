
class Solution(object):
    def numMatchingSubseq(self, S, words):
        def subseq(word):
           it = iter(S)
           return all(x in it for x in word)
        
        return sum(subseq(word) for word in words)

S = "abcde"
words = ["a", "bb", "acd", "ace"]
sol = Solution()
print(sol.numMatchingSubseq(S, words))