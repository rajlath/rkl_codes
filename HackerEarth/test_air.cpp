#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cctype>
#include <map>

using namespace std;

typedef long long LL;
LL ans;
int n,odd,even;
map<int,int> bin;

inline int read()
{
	int x=0,f=1;
	char ch=getchar();
    while ( !isdigit(ch))  f=ch=='-'?-1:f,ch=getchar();
    while ( isdigit(ch))   x=x*10+ch-'0',ch=getchar();
    return x*f;


}

int main()
{
    n=read(),bin[0]=1,ans=0;
    for (int i=1,x;i<=n;++i) x=read(),odd+=x&1,even+=(x&1)^1,ans+=bin[odd-even],++bin[odd-even];
    printf("%lld\n",ans);
	return 0;
}