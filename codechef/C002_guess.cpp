/*
3
6
because can do must we what
wedowhatwemustbecausewecan
2
hello planet
helloworld
3
ab abcd cd
abcd
*/
#include <iostream>
#include<vector>
#include<string>
#include<iomanip>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector <string> s;
        string r;
        for(int i=0;i<n;i++)
        {cin>>r;
         s.push_back(r);
        }
        string a;
        cin>>a;
        long int asize=a.size();
        long int b=0;
        long int size;
        vector <int> t;
        for(int i=0;i<n;i++)
        {
           string comp;
           for(int p=0;p<s[i].size();p++)
           comp.push_back(a[b+p]);
           size=s[i].size();
           //cout<<size<<endl;
           if(b+size-1<asize)
           if(s[i]==comp)//s[i].compare(b,b+size-1,a)==0)
           {
               //cout<<i<<endl;
               b+=size;
               t.push_back(i);
               i=-1;
           }
        }
        //cout<<b<<endl;
        if(b==asize)
        {for(int i=0;i<t.size();i++)
         cout<<s[t[i]]<<" ";
         cout<<endl;
        }

        else
        cout<<"WRONG PASSWORD"<<endl;

    }
	// your code goes here
	return 0;
}