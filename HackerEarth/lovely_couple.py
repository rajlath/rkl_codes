#include<bits/stdc++.h>
using namespace std;
int gcd(int a,int b){
//cout<<"hello"<<a<<b;
if(b==0) return a;
//cout<<"hello"<<a<<b;

return gcd(b,a%b);
}
int lcm(int a,int b){
return (a*b)/gcd(a,b);
}
int main(){
int T;
cin>>T;
while(T--){
int A,B;
cin>>A>>B;
int arr[1000];
int L= lcm(A,B);
int index=0;
while(L%2==0){
arr[index++] = 2;
//  cout<<arr[index-1]<<" , ";
L = L/2;
}
for(int i=3;i<=sqrt(L);i=i+2){
while(L%i==0){
    arr[index++] = i;
//   cout<<arr[index-1]<<" , ";
    L=L/i;
}
}
if(L>2) arr[index++] = L;
int count=1;
for(int i=1;i<index;i++){
if(arr[i]!=arr[i-1]) count++;
}
// cout<<"count  == "<<count;
int i;

for( i=2;i<=sqrt(count);i++){
if(count%i==0){
    cout<<"No\n";
    break;
}
}
if(count==1) cout<<"No\n";
else if(i>sqrt(count))
cout<<"Yes\n";
}
}