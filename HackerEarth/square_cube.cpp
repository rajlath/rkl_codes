// Square or Cube

#include <bits/stdc++.h>
using namespace std;

long long mod2 = 1073741824;
long long mod3 = 1162261467;

vector<int> prime[100005];
int zero[300005], minusOne[300005];
long long hash2[300005], hash3[300005], power2[100005], power3[100005];

long long xor2(long long a, long long b)
{
return (a ^ b) % mod2;
}

long long xor3(long long a, long long b, int flag)
{
long long ans = 0, three = 1;

while(a || b)
{
int rem = 0;

if(flag == 1)
rem = ((a%3) + (b%3))%3;
else
rem = ((a%3) - (b%3) + 3)%3;

ans += three * rem;
a /= 3, b /= 3;
three *= 3;
}

return ans % mod3;
}

int main()
{
cin.tie(NULL), cout.tie(NULL);

int N, Q;
cin >> N >> Q;

power2[0] = power3[0] = 1;
set<long long> s1, s2;

for(int i=1; i<=100000; i++)
{
power2[i] = power2[i-1] * 1000003 % mod2;
power3[i] = power3[i-1] * 1000003 % mod3;

s1.insert(power2[i]);
s2.insert(power3[i]);
}

for(int i=2; i<=100000; i++)
if(prime[i].empty())
{
for(int j=i; j<=100000; j+= i)
{
int num = j;

while(num % i == 0)
prime[j].push_back(i), num /= i;
}
}

for(int i=1; i<=N; i++)
{
int x;
cin >> x;

hash2[i] = hash2[i-1], hash3[i] = hash3[i-1];
zero[i] = zero[i-1], minusOne[i] = minusOne[i-1];

if(x == 0)
{
zero[i]++;
continue;
}

if(x < 0)
{
minusOne[i]++;
x = -x;
}

for(int j=0; j<prime[x].size(); j++)
{
hash2[i] = xor2(hash2[i], power2[ prime[x][j] ]);
hash3[i] = xor3(hash3[i], power3[ prime[x][j] ], 1);
}
}

while(Q--)
{
int L, R;
cin >> L >> R;

if(zero[R] - zero[L-1])
{
cout << "Both\n";
continue;
}

int isNeg = (minusOne[R] - minusOne[L-1]) % 2;
bool isSquare = (xor2(hash2[R], hash2[L-1]) == 0 && isNeg == 0);
bool isCube = (xor3(hash3[R], hash3[L-1], -1) == 0);

if(isSquare && isCube)
cout << "Both\n";
else if(isSquare)
cout << "Square\n";
else if(isCube)
cout << "Cube\n";
else
cout << "None\n";
}

return 0;
}