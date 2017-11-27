#include <bits/stdc++.h>
using namespace std;
map<char,char>m,m1;
map<char,char>::iterator it;
char s[1000005],s1[10];
int main()
{
    int n,i;
    cin>>n;
    char a,b,o,pp;
    while(n--)
    {
        cin>>a>>b;
        if(m.find(a)==m.end()&&m.find(b)==m.end()){
        m[a]=b;
        m[b]=a;}
        else if(m.find(a)!=m.end()&&m.find(b)!=m.end())
        {
            o=m[b];
            m[b]=m[a];
            m[a]=o;
        }
        else if(m.find(a)!=m.end()&&m.find(b)==m.end())
        {
            m[b]=m[a];
            m[a]=b;
        }
         else if(m.find(a)==m.end()&&m.find(b)!=m.end())
        {
            m[a]=m[b];
            m[b]=a;
        }

    }
    for(it=m.begin();it!=m.end();it++)
    {
        o=(*it).first;
        pp=(*it).second;
        m1[pp]=o;
        m1[pp+32]=o+32;
    }
    //fgets(s, strlen(s), stdin);
    char d;cin>>d;
    gets(s);
    if(m1.find(d)!=m1.end()) cout<<m1[d];else cout<<d;

    int l=strlen(s);
    for(i=0;i<l;i++)
    {

        if(m1.find(s[i])!=m1.end())
        {
            s[i]=m1[s[i]];
        }
    }
    for(int i=0;i<l;i++) cout<<s[i];
    return 0;
}