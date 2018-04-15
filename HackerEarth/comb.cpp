// C++ implementation to count ways to
// sum up to a given value N
#include <bits/stdc++.h>

using namespace std;

int countWays(int arr[], int m, int N)
{
    int count[N+1];
    memset(count, 0, sizeof(count));
    count[0] = 1;
    for (int i=1; i<=N; i++)
        for (int j=0; j<m; j++)
            if (i >= arr[j])
                count[i] += count[i - arr[j]];
    return count[N];
}
int main()
{
    int arr[] = {2,3,5};
    int m = sizeof(arr) / sizeof(arr[0]);
    int N = 8;
    cout << countWays(arr, m, N);
    return 0;
}


