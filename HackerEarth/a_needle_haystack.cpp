#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    string one,two;
    cin>>t;
    while(t--){
        cin>>one>>two;
        int i, j, hash[26]={0};
        for(i=0; i<one.length(); i++){
            hash[one[i]-'a']++;
        }
        int dup[26]={0};
        for(j=0; j<one.length(); j++){
                dup[two[j]-'a']++;
            }
         
        for(i=0; i<two.length()-one.length()+1;  i++){
            int flag=0;
            for(j=0; j<26; j++){
       //         cout<<dup[j]<<" ";
                if(hash[j] != dup[j])
                    flag=1;
            }
        //    cout<<endl;
            if(flag==0){
                printf("YES\n");
                break;
            }
            dup[two[i]-'a']--;
            if(i+1<two.length())
                dup[two[i+one.length()]-'a']++;
        }
        if(i==two.length()-one.length()+1)
            printf("NO\n");
    }
    return 0;
}
