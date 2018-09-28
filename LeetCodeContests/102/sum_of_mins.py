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

class Solution {
    const long M = 1000000007;
    typedef vector<int> vi;
    long sumSM(int l, int r, vi&A){
        long ans = 0;
        if(l>=r) return 0;
        if(l==r-1) return A[l];
        int idx = l, m = A[l];
        for(int i=l; i<r; ++i) if(A[i] < m){
            m = A[i];
            idx = i;
        }
        ans = long(idx+1-l) * long(r-idx) * long(m);
        ans %= M;
        ans += sumSM(l, idx, A);
        ans %= M;
        ans += sumSM(idx+1, r, A);
        ans %= M;
        return ans;
    }
public:
    int sumSubarrayMins(vector<int>& A) {
        int n = A.size();
        return int(sumSM(0, n, A));
    }
};

