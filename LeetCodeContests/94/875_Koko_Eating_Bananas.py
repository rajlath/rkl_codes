'''
Koko loves to eat bananas.
There are N piles of bananas, the i-th pile has piles[i] bananas.
The guards have gone and will come back in H hours.
Koko can decide her bananas-per-hour eating speed of K.
Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
If the pile has less than K bananas, she eats all of them instead, and won't eat any more
bananas during this hour.
Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
Return the minimum integer K such that she can eat all the bananas within H hours.

Example 1:
Input: piles = [3,6,7,11], H = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], H = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], H = 6
Output: 23

Note:
1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9
'''

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        if len(piles) == H:
            return max(piles)
        else:
            i=-(-sum(piles)//H)
            j=max(piles)
            z=j
            while i<=j:
                k=(i+j)//2
                count=0
                for q in piles:
                    count+=(-(-q//k))
                if count>H:
                    i=k+1
                else:
                    j=k-1
                    z=k

            return z

class Solution1(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        mins = 2
        maxs = max(piles)
        alls = sum(piles)
        if H >= alls:
            return 1
        while maxs > mins:
            mids = (mins + maxs) // 2
            alls = sum([(p-1)//mids+1 for p in piles])
            if alls > H:
                mins = mids+1
            else:
                maxs = mids
        return mins

#official Solution
class Solution(object):
    def minEatingSpeed(self, piles, H):
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p-1) // K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo

print(Solution1().minEatingSpeed([30,11,23,4,20],5))
print(Solution().minEatingSpeed([30,11,23,4,20],5))




