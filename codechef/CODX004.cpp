#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int a[6];
    for(int i = 0; i < 6; i++)
    {
        a[i] = s[i] - 48;
    }
    int diff;
    diff = abs(a[0] + a[1] + a[2] - a[3] - a[4] - a[5]);
    int change;
    if(diff % 9 == 0)
        change = diff/9;
    else
        change = diff/9 + 1;
    cout << change << endl;

}
