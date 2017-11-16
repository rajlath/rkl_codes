'''
#include <bits/stdc++.h>
using namespace std;
int dp[100005];
int main()
{
	int t,n;
	long long ans;
	string s;
	map <int,long long> m;
	cin >> t;
	while ( t-- ) {
		cin >> s;
		n = (int)s.size();
		assert(n<=100000);
		m.clear();
		dp[0] = 0;
		ans = 0;
		for ( int i = 1; i <= n; i++ ) dp[i] = dp[i-1]^(1<<(s[i-1]-97));
		m[dp[0]]++;
		for ( int i = 1; i <= n; i++ ) {
			ans += m[dp[i]];
			m[dp[i]]++;
		}
		cout << ans << endl;
	}
	return 0;
}
'''
for _ in range(int(input())):
    s = input()
    dp = [0] * 100005
    dp[0] = 0
    m = {}
    for i in range(1, len(s)+1):
        print(ord(s[i-1])-97)
        dp[i] = dp[i-1]^(1<<(ord(s[i-1])-97))
        m[dp[i]] = m.get(dp[i], 0) + 1
       
    print(dp[:len(s)], m)    
