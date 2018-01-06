#include <bits/stdc++.h>
using namespace std;
#define opt ios_base::sync_with_stdio(0)
#define lli long long int
#define ulli unsigned long long int
#define I int
#define S string
#define D double
#define rep(i,a,b) for(i=a;i<b;i++)
#define repr(i,a,b) for(i=a;i>b;i--)
#define in(n) scanf("%lld",&n)
#define in2(a,b) scanf("%lld %lld",&a,&b)
#define in3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define out(n) printf("%lld",n)
#define inu(a) scanf("%lld",&a)
#define outu(a) printf("%llu",a)
#define ins(s) scanf("%s",&s)
#define outs(s) printf("%s",s)
#define nl printf("\n")
#define mod 1000000007
#define inf 1000000000

#define sz() size()
typedef long long       ll;
typedef pair<lli, lli>  plli;
typedef vector<lli>     vlli;
typedef vector<ulli>    vulli;
typedef vector<ll>      vll;
typedef vector<string>  vs;
typedef vector<plli>     vplli;
#define MM(a,x)  memset(a,x,sizeof(a));
#define ALL(x)   (x).begin(), (x).end()
#define P(x)       cerr<<"{"#x<<" = "<<(x)<<"}"<<endl;
#define P2(x,y)       cerr<<"{"#x" = "<<(x)<<", "#y" = "<<(y)<<"}"<<endl;
#define P3(x,y,z)  cerr<<"{"#x" = "<<(x)<<", "#y" = "<<(y)<<", "#z" = "<<(z)<<"}"<<endl;
#define P4(x,y,z,w)cerr<<"{"#x" = "<<(x)<<", "#y" = "<<(y)<<", "#z" = "<<(z)<<", "#w" = "<<(w)<<"}"<<endl;
#define PP(x,i)     cerr<<"{"#x"["<<i<<"] = "<<x[i]<<"}"<<endl;
#define TM(a,b)     cerr<<"{"#a" -> "#b": "<<1000*(b-a)/CLOCKS_PER_SEC<<"ms}\n";
#define UN(v)    sort(ALL(v)), v.resize(unique(ALL(v))-v.begin())
#define mp make_pair
#define pb push_back
#define f first
#define s second
lli d[1001],visited[1001];
vlli v[1001];

void BFS(lli k)
{
    queue<lli>q;
    q.push(k);
    visited[k]=1;
    while(!q.empty())
    {
        k=q.front();
        q.pop();
        lli u,i;
        for(i=0;i<v[k].size();i++)
        {
            if(visited[v[k][i]]==0)
            {

                visited[v[k][i]]=1;
                d[v[k][i]]=d[k]+1;
            }

        }

    }

}
void DFS(lli k)
{
    visited[k]=1;
    cout<<k<<" ";
    lli i;
    rep(i,0,v[k].sz())
    {
        if(!visited[v[k][i]])
        {
            DFS(v[k][i]);
        }
    }
}
lli pow(lli a,lli b)
{
    lli value;
    if(b==0)
    {
        return 1;
    }
    if(b%2==0)
    {
        value=pow(a,b/2)%mod;
        return (value*value)%mod;
    }
    else
    {
        value=pow(a,b/2)%mod;
        return (((a*value)%mod)*(value))%mod;
    }
}
int main()
{
    opt;
    lli t;
    cin>>t;
    while(t--)
    {
        lli n,m,i,x,y;
        vlli ans;
        cin>>n>>m;
        lli a[m+1],b[m+1];
        rep(i,1,m+1)
        {
            cin>>a[i]>>b[i];
        }
        rep(i,1,n)
        {
            cin>>x;

            ans.pb(a[x]);
            ans.pb(b[x]);
        }
    //    cout<<ans.size()<<endl;
        //nl;
        sort(ans.begin(),ans.end());
         ans.erase( unique( ans.begin(), ans.end() ), ans.end() );

        //nl;
        if(ans.sz()==n)
        {
            cout<<"YES"<<endl;


        }
        else
        {
            cout<<"NO"<<endl;
        }
    }

}