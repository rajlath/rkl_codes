'''
890. Find and Replace Pattern
User Accepted: 1555
User Tried: 1629
Total Accepted: 1575
Total Submissions: 2100
Difficulty: Medium
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.


Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
'''
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        patts = self.matcher(pattern)
        for i in words:
            if   self.matcher(i) == patts:
                ans.append(i)
        return ans
    def matcher(self, s):
        pats = []
        last = []
        for i in s:
            if pats and pats[-1] == i:
                 last[-1] += 1
            else:
                pats.append(i)
                last.append(1)
        return "".join(map(str,last))

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word, pattern):
            m = {}
            for a, b in zip(word, pattern):
                if b in m:
                    if m[b] != a:
                        return False
                else:
                    m[b] = a
            return len(m) == len(set(m.values()))

        return [w for w in words if match(w, pattern)]



print(Solution().findAndReplacePattern(["abc","cba","xyx","yxx","yyx"],"abc"))
print(Solution().matcher("abc"))

