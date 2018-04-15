#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll c[1005];
main()
{
	ll n,m,i,min,x;
	cin>>n>>m;
	for(i=1;i<=m;i++)
	{
		cin>>x;
		c[x]++;
	}
	min=INT_MAX;
	for(i=1;i<=n;i++)
		if(c[i]<min)
			min=c[i];
		cout<<min;
}