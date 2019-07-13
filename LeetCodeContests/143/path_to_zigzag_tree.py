class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        def f(n):
            m = n.bit_length()
            if m % 2 == 1: return n
            return 3*(1<<(m-1))-n-1
        s = []
        i = f(label)
        while i:
            s = [i] + s
            i >>= 1
        return list(map(f, s))

print(Solution().pathInZigZagTree(14)   )