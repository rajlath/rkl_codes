class Solution:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """

        T = 1

        while self._DroppingMax(K, T) < N:
            T += 1
        return T

    def _DroppingMax(self, K, T):
        if K == 1:
            return T
        if K >= T:
            return 2**T - 1
        return self._DroppingMax(K, T - 1) + self._DroppingMax(K - 1, T - 1) + 1