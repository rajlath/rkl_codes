#include <bits/stdc++.h>
using namespace std;
int main() {
    freopen("C-small-practice.in", "r", stdin);
	freopen("output-small.out", "w", stdout);
    long long int t, i, n, m;
    cin>>t;
    for(i = 0; i < t; ++i){
        cout<<"Case #"<<i+1<<": ";
        cin>>n>>m;
        cout<<(min(n, m) * (min(n, m) + 1)) / 2<<endl;
    }
    return 0;
}