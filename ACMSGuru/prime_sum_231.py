'''
#include <cstdio>
#include <vector>
#include <utility>
using namespace std;
#define N (1000000)
int main()
{
  //freopen("in","r",stdin);
  int n;
  scanf("%d",&n);
  vector<bool> primes(N+1,true);
  vector<int> primenum;
  primes[0]=primes[1]=false;
  for(int i=2;i*i<=n;++i)
    if(primes[i])
      for(int j=i*i;j<=n;j+=i)
	primes[j]=false;
  vector<int>pripair;
  for(int i=5;i<=n;++i)
    if(primes[i-2] && primes[i])
      pripair.push_back(i-2);
  printf("%d\n",(int)pripair.size());
  for(int i=0;i<pripair.size();++i)
    printf("2 %d\n",pripair[i]);
  return 0;
}
'''
N = 1000000

primes = [1] * (N+1)
primes[0] = 0
primes[1] = 0
i = 2
while i * i <= N:
    if primes[i]:
        for j in range(i*i, N, i):
            primes[j] = 0
    i += 1
pripair = []
n = int(input())
for i in range(5, n+1):
    if primes[i-2] and primes[i]:
        pripair.append(i-2)
print(len(pripair))
for i in range(len(pripair)):
    print(2, pripair[i])










