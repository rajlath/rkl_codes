#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll solve(ll n,ll m)
{
    if(n==0||m==0)
        return 0;
    else if(n%2==0&&m%2==0)
        return solve(n/2,m/2); // Halving both dimensions doesn't change the number of tiles
    else if(n%2==0&&m%2==1)
        return (n+solve(n/ 2,m/ 2));// Use a row of 1x1 tiles
    else if(n%2==1&&m%2==0)
        return (m+solve(n/ 2,m/ 2));// Use a column of 1x1 tiles
    else
        return (n+m-1+solve(n/2,m/2)); //ROW OR COLUMN (WHICHEVER OVERLAP)
}
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n,m,i,j,p,q,r;
        cin>>n>>m;
        cout<<solve(n,m)<<endl;
    }
}