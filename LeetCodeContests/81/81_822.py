'''
Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.
'''
class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        elig=[-1]*2001
        for i,j in zip(fronts,backs):
            if i==j:
                elig[i]=0
            else:
                if elig[i]==-1:
                    elig[i]=1
                if elig[j]==-1:
                    elig[j]=1
        for i in range(1,2001):
            if elig[i]==1:
                return i
        return 0


'''
sol by crazymerlin
'''
from collections import defaultdict
class Solution(object):
    def flipgame1(self, fronts, backs):
        possib = defaultdict(lambda : True)
        for a, b in zip(fronts, backs):
            if a == b:
                possib[a] = False

        possibs = [x for x in fronts + backs if possib[x]]


        return min(possibs) if possibs else 0


sol = Solution()
print(sol.flipgame1([1,2,4,4,7], [1,3,4,1,3]))