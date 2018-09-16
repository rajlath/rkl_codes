'''
870. Advantage Shuffle
User Accepted: 925
User Tried: 1365
Total Accepted: 939
Total Submissions: 2872
Difficulty: Medium
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for
which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
'''
#solution by https://leetcode.com/yangzhenjian
class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        a = sorted([(x, i) for i,x in enumerate(A)])
        b = sorted([(x, i) for i,x in enumerate(B)])
        i, j = 0, 0
        k = -1
        ans = [0] * n
        while i < n and j < n:
            if a[i][0] > b[j][0]:
                ans[b[j][1]] = a[i][0]
                j += 1
            else:
                ans[b[k][1]] = a[i][0]
                k -= 1
            i += 1
        return ans

#solution by awice
#class Solution(object):
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]

