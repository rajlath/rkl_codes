#include<iostream>
using namespace std;
int main()
{
int t,N,M,sum;
cin>>t;
while(t--)
  {   sum=0;
      cin>>N>>M;
      if(M==0 || N==0)
      {
          cout<<"0";
        }
        else
        {
      sum=(N-1)+(M-1)+2*((N-1)*(M-1));
      cout<<sum<<endl;
        }
  }
return 0;
}