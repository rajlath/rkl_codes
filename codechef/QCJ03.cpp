#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long
#define double long double

int32_t main()
{
    IOS;
    int n;
    cin>>n;
    int arr[n+1]={};
    int summ=0;
    for(int i=1;i<=n;i++)
    {
        cin>>arr[i];
        summ+=arr[i];
    }
    int m=0;
    int s[n+1]={};
    for(int i=1;i<=n;i++)
    {
        m++;
        s[m]=arr[i];
        while(m>=3&&s[m-2]<=s[m-1]&&s[m-1]>=s[m])
        {
            s[m-2]=s[m-2]-s[m-1]+s[m];
            m-=2;
        }
    }
    cout<<m<<endl;
    int value=0,sign=1;
    int i=1,j=m;
    while(i<=j)
    {
        if(s[i]>=s[j])
        {
            value+=sign*s[i];
            i++;
        }
        else
        {
            value+=sign*s[j];
            j--;
        }
        sign=-sign;
        cout<<value<<endl;
    }
    cout<<(summ+value)/2;

}