#include<bits/stdc++.h>
using namespace std;


int main()
{
    int nb_test;
    cin>>nb_test;
    while (nb_test > 0)
    {
        int lens, res=0;
        cin>>lens;
        int arr[lens+1];
        for(int i = 0; i < lens; i++)
        {
            cin>>arr[i];
        }
        for (int i = 0; i < lens; i++)
        {
            for(int j = i; j < lens; j++)
            {
                int curr;
                curr = arr[i] ^ arr[j];
                if ((curr%2==0) && (curr != 2) && (curr != 0))
                {
                    res ++;

                }
            }
        }
        cout << res << "\n";
        nb_test --;
    }


}