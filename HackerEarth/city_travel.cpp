#include <iostream>
#include <vector>
#define l long long int
using namespace std;
int main()
{
    l s,x,n;
    cin>>s>>x>>n;

    l sum=0;
    l excep[n][2]={};
    for (l i=0;i<n;i++)
    {
        cin>>excep[i][0]>>excep[i][1];
    }
    for (l i=0;i<n-1;i++)
    {
        l mini=i;
        for (l j=i+1;j<n;j++)
        {
            if (excep[mini][0]>excep[j][0])
            mini=j;
        }
        swap(excep[i][0],excep[mini][0]);
        swap(excep[i][1],excep[mini][1]);
    }
    l j=0;
    l i=0;
    for (i=1;sum<s;i++)
    {
        if (excep[j][0]==i)
        {
            sum+=excep[j][1];
            j++;
        }
        else
        sum+=x;
    }
    cout<<i-1<<endl;
return 0;
}