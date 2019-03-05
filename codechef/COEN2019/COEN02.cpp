#include <bits/stdc++.h>
using namespace std;
bool check(pair<int,int> a,pair<int,int> b){
    if(a.first<=b.first&&a.second<=b.second)
        return false;
    swap(a.first,a.second);
    if(a.first<=b.first&&a.second<=b.second)
        return false;
    return true;
}
int main(){
    int t=1;
    while(t--){
        int n;
        cin >> n;
        vector<pair<int,int> > v(n);
        for(int i = 0; i < n;i++){
            cin >> v[i].first;
        }
        for(int i=0;i<n;i++){
            cin >> v[i].second;
            if(v[i].first<v[i].second){
                swap(v[i].first,v[i].second);
            }
        }
        sort(v.begin(),v.end());
        int dp[n+5]={0};
        int ans=1;
        for(int i=n-1;i>=0;i--){
            dp[i]=1;
            for(int j=n-1;j>=i;j--){
                if(check(v[i],v[j])){
                    dp[i]=max(dp[j]+1,dp[i]);
                }
            }
            ans=max(ans,dp[i]);
        }
        cout << ans << "\n";
    }
}