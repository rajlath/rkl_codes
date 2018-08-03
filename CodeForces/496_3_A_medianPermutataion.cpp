
#include<bits/stdc++.h>
using namespace std;
map<int,int>ma;
int main()
{
	ma[0]=1;
	int n,m,s=0,fla=0;
	long long ans=0;
	cin>>n>>m;
	for(int i=1;i<=n;i++)
	{
		int k;
		scanf("%d",&k);
		if(k==m)
		{
			fla=1;
		}
		else if(k<m)
		{
			s--;
		}
		else if(k>m)
		{
			s++;
		}
        cout<<fla<<" "<<s<<" "<<ma[s]<<endl;
		if(fla==0)ma[s]++;

		if(fla)
		{
			//cout<<ans<<endl;
			ans=ans+ma[s]+ma[s-1];
		}
	}
	cout<<ans<<endl;
	return 0;
}
