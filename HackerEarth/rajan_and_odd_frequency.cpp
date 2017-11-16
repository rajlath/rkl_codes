#include<bits/stdc++.h>
using namespace std;
int a[200006];
int main()
{
    int n;
    //freopen("in09.txt","r",stdin);
    //freopen("out09.txt","w",stdout);
    scanf("%d",&n);
    int i;
    int d=2*n+1;
    for(i=0;i<d;i++)
        scanf("%d",&a[i]);
    int ans=0;
    for(i=0;i<d;i++)
        ans=ans^a[i];
    printf("%d\n",ans);

}
