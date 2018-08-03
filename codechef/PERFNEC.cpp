/*
	Author: @himkha_100
*/
#include<bits/stdc++.h>
#define mod 1000000007
#define ll long long int
#define s(t) scanf("%d",&t)
#define p(t) printf("%d\n",t)
#define pb push_back
using namespace std;
int main()
{
	int s,g,q,r,d;
	cin>>s>>g>>q>>r>>d;
	int Q;
	cin>>Q;
	ll dp[101][402];
	for(int i=0;i<101;i++)
	{
		for(int j=0;j<402;j++)
		{
			dp[i][j]=1000000000;
		}
	}
	ll x1,y1,a1;
	for(int i=0;i<=100;i++)
	{
		for(int j=0;j<=100-i;j++)
		{
			for(int k=0;k<=100-i-j;k++)
			{
				for(int l=0;l<=100-i-j-k;l++)
				{
					for(int m=0;m<=100-i-j-k-l;m++)
					{
						x1=i+j+k+l+m;
						y1=(-2*i)+(-j)+l+(2*m);
						a1=(s*i)+(g*j)+(q*k)+(r*l)+(d*m);
						dp[x1][y1+200]=min(dp[x1][y1+200],a1);
					}
				}
			}
		}
	}
	while(Q--)
	{
	int x,y;
	cin>>x>>y;
	if(dp[x][y+200]!=1000000000)
	cout<<dp[x][y+200]<<endl;
	else
	cout<<"-1\n";
	}
	return 0;
}
