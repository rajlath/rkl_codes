class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        AB = A * B
        st = set()
        for i in range(A, AB+1, A):
            st.add(i)
        for i in range(B, AB, B):
            st.add(i)
        sts = sorted(list(st))
        N -= 1
        c = len(sts)
        ans = (N//c) * AB
        N%=c
        ans += sts[N]
        print(sts)
        return ans % 1000000007

print(Solution().nthMagicalNumber(5, 2, 4))
