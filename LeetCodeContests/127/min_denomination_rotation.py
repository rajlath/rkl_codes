class Solution(object):
    ef minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        a = collections.Counter(A)
        b = collections.Counter(B)
        c = a + b
        m = c.most_common(1)[0]
        if m[1] < n:
            return -1
        cand = m[0]
        ac, bc = 0, 0
        for i in range(n):
            if cand != A[i]:
                if cand != B[i]:
                    return -1
                ac += 1
            elif cand != B[i]:
                bc += 1
        return min(ac, bc)