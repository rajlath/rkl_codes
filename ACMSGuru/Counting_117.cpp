#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <utility>
#include <string.h>
#include <stdlib.h>
#include <functional>
using namespace std;
typedef long long ll;

int gcd(int a,int b)
{
    return (b==0?a:gcd(b,a%b));
}

int can(int t,int m,int k)
{
    if(m==1 || t==1)
        return t%k==0;

    int d=gcd(t,k);
    cout<<t<<" "<<k<<" "<<d<<"\n";
    return can(d,m-1,k/d);
}

int main()
{


    int n,m,k;
    cin>>n>>m>>k;


    int ans=0;
    for(int i=0,t;i<n;++i)
    {

        cin>>t;
        if(can(t,m,k))
            ++ans;
    }
    cout<<ans;


    return 0;
}