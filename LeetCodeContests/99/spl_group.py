class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        lens = len(A)
        groups=[]
        for i in range(lens):
            curr = A[i]
            grps = [curr]
            for j in range(lens):
                if i != j and A[j] in curr+curr and A[j] not in grps:
                        grps.append(A[j])
            groups.append(grps)
        return len(groups)

print(Solution().numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))
