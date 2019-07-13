#include <bits/stdc++.h>
using namespace std;


int coinChange(vector<int>& coins, int amount) {
    vector<int> v(amount + 1, amount + 1);
    v[0] = 0;
    for(int i = 1; i <= amount; i++)
        for(int c : coins)
            if(i >= c) v[i] = min(v[i], v[i - c] + 1);
    return v.back() > amount ? -1 : v.back();
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, amt, input;
    cin >> n >> amt;
    vector<int> coins;
    for (int i = 0; i < n; i++)
    {
        cin>>input;
        coins.push_back(input);
    }
    int answer = coinChange(coins, amt);
    cout<<answer<<endl;


}