'''
930. Binary Subarrays With Sum

In an array A of 0s and 1s, how many non-empty subarrays have sum S?



Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
'''

from collections import defaultdict
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        prev_sum = defaultdict(int)
        curr_sum = 0
        counts   = 0
        lens = len(A)
        for i in range(lens):
            curr_sum += A[i]
            if curr_sum == S:
                counts += 1
            t = curr_sum - S
            if t in prev_sum:
                counts += prev_sum[t]
            prev_sum[curr_sum] += 1
        return counts

print(Solution().numSubarraysWithSum([1,0,1,0,1],2))

from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        d=defaultdict(lambda:0)
        ps=0
        ans=0
        for a in A:
            d[ps]+=1
            ps+=a
            ans+=d[ps-S]
        return ans



