#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

string make_change(vector<int> coins, int money) {

    long long combo[money+1]={0};
    combo[0]=1;
    int coinCount = coins.size();
    int currCoin;
    for(int i=0;i<coinCount;i++)
    {
        currCoin = coins[i];
        for(int j=currCoin;j<=money;j++)
        {
            if(j>=currCoin)
            {
                combo[j]+=combo[j-currCoin];
            }
        }
    }
    return std::to_string(combo[money]);

}

int main(){
    int n;
    int m;
    cin >> n >> m;
    vector<int> coins(m);
    for(int coins_i = 0;coins_i < m;coins_i++){
    cin >> coins[coins_i];
    }
    string output = make_change(coins, n);
    cout << output << endl;
    return 0;
}