#include<bits/stdc++.h>
using namespace std;
const int N=1010,p=1e9+7;
int n,aa,bb,pa,pb,f[N][N];
inline int qmi(int x,int y){
	int ans=1;
	for (;y;y>>=1,x=1ll*x*x%p) if (y&1) ans=1ll*ans*x%p;
	return ans;
}
inline int inv(int x){
	return qmi(x,p-2);
}
int main(){
	scanf("%d%d%d",&n,&aa,&bb);
	pa=1ll*aa*inv(aa+bb)%p;
	pb=1ll*bb*inv(aa+bb)%p;
	f[1][0]=1;
	int ans=0,tmp=1ll*pa*inv(pb)%p;
	for (int i=1;i<=n;++i)
		for (int j=0;j<=n;++j)
		if (i+j>=n){
			ans+=1ll*f[i][j]*(i+j+tmp)%p;
			ans%=p;
		}else{
			f[i+1][j]=(f[i+1][j]+1ll*f[i][j]*pa)%p;
			f[i][j+i]=(f[i][j+i]+1ll*f[i][j]*pb)%p;
		}
	printf("%d",ans);
	return 0;
}