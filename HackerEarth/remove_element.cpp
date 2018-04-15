// Remove the element

#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007

long long A[100005], fact[100005];

int main()
{
int T;
cin >> T;

fact[0] = 1;

for(int i=1; i<=100000; i++)
fact[i] = fact[i-1] * i % MOD;

while(T--)
{
int N;
cin >> N;

for(int i=1; i<=N; i++)
cin >> A[i];

sort(A+1, A+1+N);
reverse(A+1, A+1+N);

long long ans = 0;

for(int i=1; i<=N; i++)
ans += A[i] * fact[i] % MOD;

cout << ans % MOD << "\n";
}

return 0;
}