#include<cmath>
#include<cstdio>
#include<cstring>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

const int maxn = 1000000 + 100;
const int Size = 100000;
int prime[Size], cnt;
bool mark[maxn];
vector<int> ans;

void sieve(int n)
{
    int i, j;
    cnt = 1, prime[0] = 2;
    for(i=3; i<=n; i += 2)
    {
        if(!mark[i]) prime[cnt++] = i;
        for(j=1; j<cnt && prime[j]<=n/i; ++j)
        {
            mark[i*prime[j]] = 1;
            if(!(i%prime[j])) break;
        }
    }
}

int main()
{
    int n, i;
    scanf("%d", &n);
    sieve(n);
    for(i=1; i<cnt; ++i)
    {
        if(prime[i] - prime[i-1] == 2)
        {
            ans.push_back(i-1);
        }
    }
    printf("%d\n", ans.size());
    for(i=0; i<ans.size(); ++i)
    {
        printf("2 %d\n", prime[ ans[i] ]);
    }
    return 0;
}