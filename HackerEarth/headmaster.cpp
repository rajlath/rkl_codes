#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long

int main()
{
    ull L, R;
    cin >> L >> R;
    vector<ull> num;
    string temp;
    for(ull i = L; i <= R; i++)
    {
        temp = to_string(i);
        sort(temp.begin(),temp.end());
        ull j = 0;
        while(temp[j] == '0' && j < temp.size())
            j++;
        temp = temp.substr(j);

        num.push_back(stoi(temp));
    }

    sort(num.begin(),num.end());
    ull ctr = 1;
    for(ull i = 1; i < num.size(); i++)
        if(num[i] != num[i-1])
            ctr++;

    cout << ctr << endl;
}