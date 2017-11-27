#include <iostream>
#define MOD 1000000007
#include <bits/stdc++.h>
using namespace std;


long long fast_power(long long base, long long power) {
    long long result = 1;
    while(power > 0) {

        if(power % 2 == 1) { // Can also use (power & 1) to make code even faster
            result = (result*base) % MOD;
        }
        base = (base * base) % MOD;
        power = power / 2; // Can also use power >>= 1; to make code even faster
    }
    return result;
}

int main()
{
     int n, i;
     long long ans;
     cin >> n;
     while (n > 0)
     {
         cin >> i;
         ans = (2 * fast_power(3, i) - 1) % MOD;
         cout<<ans<<"\n";
         n--;


        }

}

