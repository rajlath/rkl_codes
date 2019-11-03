class Solution:
    def maximumSum(self, arr):
        n = len(arr)
        pref = [0]*n
        suff = [0]*n
        curr = 0
        for i in range(n):
            pref[i] = curr = max(curr, 0) + arr[i]
        curr = 0
        for i in range(n-1,-1,-1):
            suff[i] = curr = max(curr, 0) + arr[i]
        return max(pref + suff + [pref[i-1] + suff[i+1] for i in range(1,n-1)])

class Solution:
def maximumSum(self, A) -> int:
    cumsum = []
    prev = 0
    for i in A:
        prev += i
        cumsum.append(prev)
    f0 = 0
    f1 = float("Inf")
    f2 = float("Inf")
    ans = A[0]
    for i in range(len(A)):

        ans = max(ans, cumsum[i] - f0)

        ans = max(ans, cumsum[i] - f1)

        ans = max(ans, cumsum[i] - f2)

        f2 = min(f2, f1 + A[i])
        f1 = min(f1, f0)
        f0 = min(f0, cumsum[i])

    return ans