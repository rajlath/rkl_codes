'''
A sequence X_1, X_2, ..., X_n is fibonacci-like if:
n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence,
find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.
(Recall that a subsequence is derived from another sequence A by deleting any number of elements
(including none) from A, without changing the order of the remaining elements.
For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

Example 1:
Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:
Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
'''
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        visited = {}
        As   = set(A)
        len_A   = len(A)
        best  = 0

        for i in range(len_A):
            for j in range(i+1, len_A):
                a, b = A[i], A[j]
                mlen = 2
                while a+b in As:
                    a, b = b, a + b
                    mlen += 1
                    if (a,b) not in visited:
                        visited[(a, b)] = mlen
                    else:
                        if visited[(a, b)] >= mlen:
                            break
                if mlen > 2:
                    best = max(best, mlen)

        return best
#official solution
class Solution1(object):
    def lenLongestFibSubseq(self, A):
        S = set(A)
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                """
                With the starting pair (A[i], A[j]),
                y represents the future expected value in
                the fibonacci subsequence, and x represents
                the most current value found.
                """
                x, y = A[j], A[i] + A[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0


print(Solution1().lenLongestFibSubseq([1,2,3,4,5,6,7,8]))





