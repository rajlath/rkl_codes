#include<bits/stdc++.h>
using namespace std;
#define ll int
#define N 1000000007
void update(ll res[],ll l,ll r,ll val){
	res[l-1]+=val;
	res[l-1]%=N;
	res[r]-=val;
	res[r]%=N;
}
void updatearr(ll arr[],ll l,ll r,ll val){
	arr[l-1]+=val;
	arr[l-1]%=N;
	arr[r]-=val;
	arr[r]%=N;
}
 
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll t,n,m,sum,i,j,l1,r1;
	cin>>t;
	while(t--){
		cin>>n>>m>>l1>>r1;
		ll arr[m+1],res[n+1],opt[m][3];
		for(i=0;i<=n;i++)res[i]=0;
		for(i=0;i<m;i++){
			arr[i]=0;
			cin>>opt[i][0]>>opt[i][1]>>opt[i][2];
		}arr[m]=-1;
		arr[0]=1;
		sum=0;
		for(i=m-1;i>=0;i--){
			sum-=arr[i+1];
			if(sum<0)sum+=N;
			sum%=N;
			if(opt[i][0]==1)update(res,opt[i][1],opt[i][2],sum);
			else{
				updatearr(arr,opt[i][1],opt[i][2],sum);
			}
			
		}
		sum=0;
		for(i=0;i<n;i++){
			sum+=res[i];
			if(sum<0)sum+=N;
			sum%=N;
			cout<<sum<<' ';
		}
		cout<<endl;
	}
	return 0;
}		
