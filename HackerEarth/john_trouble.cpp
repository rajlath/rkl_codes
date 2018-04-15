#include<bits/stdc++.h>
    #define ull unsigned long long
    #define l 10000000000
    using namespace std;
    int main(){
        ull t;
        cin>>t;
        while(t--){
            string s1,s2;
            vector <int> a;
            cin>>s1>>s2;
            ull len1=(s1.size())%l;
            ull len2=(s2.size())%l;
            if(len2<=len1){
            for(ull i=0;i<=abs(len1-len2);i++){
                ull k=i%l,count=0;
                for(ull j=0;s2[j]!=0;j++){
                    if(s2[j]!=s1[k]){
                        count++;
                    }
                    if(count>1){
                        break;
                    }
                    k++;
                }
                if(count==1 || count==0){
                    a.push_back(i);
                }
            }
            if(a.size()==0){
                cout<<"No Match!"<<endl;
            }
            else{
            for(ull i=0;i<a.size();i++){
                cout<<a[i]<<" ";
            }}cout<<endl;}
            else{
                cout<<"No Match!"<<endl;
            }
        }
    }