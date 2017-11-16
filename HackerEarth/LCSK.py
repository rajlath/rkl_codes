dp=   [1 for x in range(2005) for y in range(2005) for z in range(6)]
print(dp[1000][1000][1])

def get_answer(n, m, k):
    global dp
    ans = dp[n][m][k]
    if ans == -1:return ans
    ans = 0
    if n == 0 or m == 0: return ans
    ans = max(get_answer(n, m-1, k), get_answer(n-1, m, k))
    if a[n] == b[m]:
        ans = max(ans, get_answer(n-1,m-1, k)+1)
    if k:
        ans = max(ans, get_answer(n-1, m-1, k-1) + 1)  
    return ans      
'''    
int f(int n, int m, int k){
	int &ans = dp[n][m][k];
	if(ans != -1)
		return ans;
	ans = 0;
	if(n == 0 || m == 0)
		return ans;
	ans = max(f(n, m - 1, k), f(n - 1, m, k));
	if(A[n] == B[m])
		ans = max(ans, f(n - 1, m - 1, k) + 1);
	if(k)
		ans = max(ans, f(n - 1, m - 1, k - 1) + 1);
	return ans;
}

n, m, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(get_answer(n,m,k))
'''




