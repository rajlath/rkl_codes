#include <iostream>
#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int prime(int number)
{
    int i = 1;
    bool is_prime = true;
    if (number == 2 || number == 1){ return true; }
    for(i = 2; i < sqrt(number); i++)
    {
        if(number % i == 0)
        {
            is_prime = false;
            break;
        }
    }

    return is_prime;
}

int main()
{
    long long signed int t, a, n, x,power_val, i, j, digsums, count = 0;
    cin>>t;
    while (t--)
    {
        cin>>a>>n;
        digsums = 0;
        power_val = pow(a, n);
        while (power_val > 0)
        {
            digsums += (power_val % 10);
            power_val /= 10;

        }

        string ans = prime(digsums) ? "1" : "0";
        cout<<ans<<endl;

    }
}


