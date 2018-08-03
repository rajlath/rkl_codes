'''
854. K-Similar Strings

Difficulty: Hard
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times
so that the resulting string equals B.
Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2
Note:

1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}

'''
class Solution:


    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        def search(curr, target, i, swapped):
            if i >= len(curr):return swapped
            if curr[i] == target[i]:return search(curr, target, i+1, swapped)
            mins = 10000
            for j in range(i+1,len(curr)):
                if curr[j] != target[i]:continue
                curr[i], curr[j] = curr[j], curr[i]
                mins = min(mins, search(curr, target, i+1, swapped+1))
                curr[i], curr[j] = curr[j], curr[i]
            return mins
        A = [x for x in A]
        B = [x for x in B]

        return search(A, B, 0, 0)


sol = Solution()
print(sol.kSimilarity("abac", "baca"))

