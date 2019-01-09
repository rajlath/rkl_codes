class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        lens = len(A)
        mlen = len(A[0])
        nb_idx = 0
        for i in range(mlen):
            curr = 'a'
            for j in range(lens):
                if A[j][i] < curr:
                    ans += 1
                    break
            curr = A[j][i]
        return ans


