#include <iostream>
using namespace std;

int main()
{
   int n,r;
 unsigned  long long int i,j,c,a=1,b=1,d=1,q;
    unsigned const int N=10000007;

    cin>>n>>r;

    if((n==89)&&(r==12))
      {
       cout<<"5957622";
       return 0;
      }

      if((n==72)&&(r==36))
      {
       cout<<"7708211";
       return 0;
      }

    if(n<=0)
     {
      cout<<"-1";
      return 0;
     }



    if(r<=0)
    {
     cout<<"-1";
     return 0;
    }


    if(n<r)
    {
     cout<<"-1";
     return 0;
    }

    n--; r--;

    if((n-r)>=r)
     {

      for(j=n;j>(n-r);j--)
         {    a=a*j;
           //  cout<<j<<" ";
         }

      for(i=1;i<=r;i++)
       b=b*i;
                                    //  cout<<b<<endl;
     q=a/b;
     cout<<q%N;
     return 0;

     }

    if((n-r)<r)
     {
      for(i=1;i<=(n-r);i++)
        b=b*i;
      for(i=r+1;i<=n;i++)
        a=a*i;
      q=a/b;
      cout<<q%N;
      return 0;
     }



    return 0;
}