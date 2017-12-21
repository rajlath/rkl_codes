#include <bits/stdc++.h>
using namespace std;

int main()
{
   int t,n,a[100001]={0};
   cin >> t;
   while(t--)
   {
       int hash[50003]={0};
       int flag=1;
       cin >> n;
       for(int i = 1; i <= n; i++)
       {
           scanf("%d",&a[i]);
           hash[a[i]]++;
       }
       int dist=1;
       int kills=0;
       for(int i = 1; i <= 50000; i++)
       {
           if(hash[i])
           {
               while(hash[i] && dist>0)
               {
                   hash[i]--;
                   dist--;
                   kills++;
                   if(kills%6==0)
                   dist--;
               }
           }
           if(hash[i])
           {
               flag=0;
               cout<<"Goodbye Rick"<<endl;
               cout<<kills<<endl;
               break;
           }
           dist++;
       }

       if(flag)
       {
           cout<<"Rick now go and save Carl and Judas"<<endl;
       }
   }
    return 0;
}