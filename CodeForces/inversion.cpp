#include<bits/stdc++.h>
#include<unordered_map>
using namespace std;
typedef double D;
typedef long long ll;
const ll mod=1e9+7;
const ll inf=(1ll<<62);
const int MX=2e5+9;
const int SQ=400;
ll n,m,a[MX],answer[MX],bit[MX*5],ans,tt;
map<int,int>hashy;
struct NODE{
    int l,r,ind;
}q[MX];
bool operator <(const NODE&A,const NODE&B){
    if((A.l/SQ)!=(B.l/SQ))return (A.l/SQ)<(B.l/SQ);
    return A.r<B.r;
}
void add(int x,int v){
    while(x<MX*2){
        bit[x]+=v;
        x+=x&-x;
    }
}
ll get(ll x){
    ll ret=0;
    while(x){
        ret+=bit[x];
        x-=x&-x;
    }
    return ret;
}
ll F(int x,int y){
    if(y==1)return get(x-1);
    if(y==2)return get(MX)-get(x);
}
int main(){
    cin>>n;
    for(int i=0;i<n;i++){scanf("%lld",&a[i]);hashy[a[i]]=1;}
    for(auto pp:hashy){
        hashy[pp.first]=++tt;
    }
    for(int i=0;i<n;i++)a[i]=hashy[a[i]];
    cin>>m;
    for(int i=0;i<m;i++){
        scanf("%d%d",&q[i].l,&q[i].r-1);
        q[i].l--;
        q[i].r--;
        q[i].ind=i;
    }
    sort(q,q+m);
    int mo_left=0,mo_right=-1;
    for(int i=0;i<m;i++){
        int L=q[i].l,R=q[i].r;
        while(mo_right<R){
            add(a[++mo_right],1);
            ans+=F(a[mo_right],2);
        }
        while(mo_right>R){
            add(a[mo_right--],-1);
            ans-=F(a[mo_right+1],2);
        }
        while(mo_left<L){
            add(a[mo_left++],-1);
            ans-=F(a[mo_left-1],1);
        }
        while(mo_left>L){
            add(a[--mo_left],1);
            ans+=F(a[mo_left],1);
        }
        answer[q[i].ind]=ans;

    }
    for(int i=0;i<m;i++)
    {
        cout<<answer[i]<<endl;
    }

}