#include<bits/stdc++.h>
using namespace std;


typedef long long ll;


int main()
{
    ios_tie();
    //cout << "除数不能为0！程序终止！" << endl;
    string s;
    ll c,p;
    cin>>s>>c>>p;
    ll ans = 0;
    loop(i,0,sz(s)-1)
    {
        for(ll j=i;j<i+25;j++)
        {
            if(j<sz(s))
            {
                ll num = 0;
                ll bin = 1;
                for(ll k=j;k>=i;k--)
                {
                    num+=(s[k]-'0')*bin;
                    bin*=2;
                }
                if(num==c)
                {
                    for(ll k=j+1;k<j+26;k++)
                    {
                        if(k<sz(s))
                        {
                            ll num2 = 0;
                            ll bin2 = 1;
                            for(ll l=k;l>=j+1;l--)
                            {
                                num2+=(s[l]-'0')*bin2;
                                bin2*=2;
                            }
                            if(num2==p)
                                ans++;
                        }
                    }
                }
            }
        }
    }
    cout<<ans;
    return 0;
}
Language: C++14