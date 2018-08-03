#include<bits/stdc++.h>
#define N 5000005
using namespace std;
int n,cnt,a[N];
int main(){
	scanf("%d",&n);
	for (int i=1;i<=n;i++) scanf("%d",&a[i]);
	for (int i=1;i<=n;i++) while (a[i]!=i) swap(a[i],a[a[i]]),cnt++;
	if ((n*3-cnt)&1) puts("Um_nik");
	else puts("Petr");
	return 0;
}