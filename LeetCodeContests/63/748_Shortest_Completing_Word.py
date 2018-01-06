'''
748. Shortest Completing Word My SubmissionsBack to Contest

Difficulty: Easy
Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate.
Such a word is said to complete the given string licensePlate
Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.
It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.
The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP",
the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.
Note:
licensePlate will be a string with length in range [1, 7].
licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
words will have a length in the range [10, 1000].
Every words[i] will consist of lowercase letters, and have length in range [1, 15].
'''
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtyp
        """
        lp = licensePlate.lower()
        lpl= [x for x in list(lp) if x.isalpha()]
        lplc= Counter(lpl)

        def is_valid(src, tgt):
            for key in src:
                if key in tgt:
                    if src[key] > tgt[key]:
                        return False
                else:return False
            return True

        ans = None
        for word in words:
            if is_valid(lplc, Counter(list(word))):
                if ans == None: ans = word
                else:
                    if len(word) < len(ans):
                        ans = word
        return ans



sol = Solution()
print(sol.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]))