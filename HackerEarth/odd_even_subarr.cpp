// Odd-Even Subarrays
#include <bits/stdc++.h>
using namespace std;

int A[200005];
map<int, int> M;

int main()
{
int N;
cin >> N;

for(int i=1; i<=N; i++)
{
cin >> A[i];

if(A[i] % 2)
A[i] = 1;
else
A[i] = -1;
}

M[0] = 1;
int pre = 0;
long long ans = 0;

for(int i=1; i<=N; i++)
{
pre += A[i];

if(M.count(pre))
ans += M[pre];

M[pre]++;
}
for(auto elem : M)
{
   std::cout << elem.first << " " << elem.second << "\n";
}
cout << ans << "\n";
return 0;
}