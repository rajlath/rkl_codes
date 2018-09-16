class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        st = []
        right_low = [0]*(n+1)
        DP        = [0]*(n+1)
        right_low[n] = n+1
        st.append(n)
        for i in range(n-1, -1, -1):
            while st and A[st[-1]] >= A[i]:
                st.pop()
            if not st:right_low[i] = n+1
            else:right_low[i] = st[-1]
            st.append(i)
        DP[n] = A[n-1]
        for i in range(n-1, 0, -1):
            DP[i] = (right_low[i]-i)*A[i] + DP[right_low[i]]
        ans = sum(DP[1:n+1])
        return ans

print(Solution().sumSubarrayMins([3,1,2,4]))

