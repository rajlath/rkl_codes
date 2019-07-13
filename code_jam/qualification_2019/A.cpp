/*
input
3
4
940
4444
output
Case #1: 3 1
Case #2: 930 10
Case #3: 3333 1111

 */
#include<bits/stdc++.h>
using namespace std;
using vi=vector<int>;
int main(){
ios::sync_with_stdio(0);
cin.tie(0);
int t;
cin>>t;
for(int T=1;T<=t;T++){
    string s;
    cin>>s;
    int n=s.size();
    vi a(n),b(n);

    for(int i=0;i<n;i++){
    a[i]=s[n-i-1]-'0';
    if(a[i]==4){
        a[i]--;
        b[i]=1;
    }
    }
    for(int x : a) cout<<x;
    cout<<endl;
    for(int x : b) cout<<x;
    cout<<endl;
    while(!b.back())b.pop_back();
    for(int x : b) cout<<x;
    reverse(a.begin(),a.end());
    reverse(b.begin(),b.end());
    cout<<"Case #"<<T<<": ";
    for(int x:a)cout<<x;
    cout<<" ";
    for(int x:b)cout<<x;
    cout<<"\n";
}
}