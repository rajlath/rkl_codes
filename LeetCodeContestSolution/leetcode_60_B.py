'''
734. Sentence Similarity My SubmissionsBack to Contest

Given two sentences words1, words2 (each represented as an array of strings),
and a list of similar word pairs pairs, determine if two sentences are similar.
For example, "great acting skills" and "fine drama talent" are similar,
if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
Note that the similarity relation is not transitive.
For example, if "great" and "fine" are similar, and "fine" and "good" are similar,
"great" and "good" are not necessarily similar.
Also, a word is always similar with itself.
For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar,
even though there are no specified similar word pairs.

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
'''
class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        def checkpair(plist, sr1, sr2):
            cnt = 0
            for x in plist:
                if sr1 in x and sr2 in x:
                    cnt += 1
            return cnt > 0


        len1 = len(words1)
        len2 = len(words2)
        if len1 != len2:return False
        for i, v in enumerate(words1):
            if v == words2[i]:continue
            a = v
            b = words2[i]
            if not checkpair(pairs, a, b):
                return False
        return True
a = ["an","extraordinary","meal","meal"]
b = ["one","good","dinner"]
p = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]

sol = Solution()
print(sol.areSentencesSimilar(a, b, p))


from collections import defaultdict
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        similar = defaultdict(set)
        for a,b in pairs:
            similar[a].add(b)
            similar[b].add(a)
        for a,b in zip(words1,words2):
            if a == b: continue
            if a not in similar[b] and b not in similar[a]:
                return False
        return True
