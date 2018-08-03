#include <bits/stdc++.h>
using namespace std;


int main()
{
	int N;
	cin>>N;
	long long A[101010];
	for(int i=0;i<N;i++)
		cin>>A[i];
	long long ans=0;
	int cnt=0;
	for(int j=62;j>=0;j--)
	{
		for(int i=cnt;i<N;i++)
		{
			if( A[i] & (1LL<<j) )
			{
				long long t=A[i];
				A[i]=A[cnt];
				A[cnt]=t;
				for(int k=0;k<N;k++)
					if(cnt!=k && (A[k] & (1LL<<j) ) )
						A[k]^=A[cnt];
				cnt++;
				break;
			}
		}
	}
	for(int i=0;i<cnt;i++)  ans^=A[i];
	cout<<ans;
}