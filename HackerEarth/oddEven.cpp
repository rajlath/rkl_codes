#include <iostream>
#include <unordered_map>
using namespace std;
/*
// Function to print all sub-arrays with 0 sum present
// in the given array
void printallSubarrays(int arr[], int n)
{
    // consider all sub-arrays starting from i
    for (int i = 0; i < n; i++)
    {
        int sum = 0;

        // consider all sub-arrays ending at j
        for (int j = i; j < n; j++)
        {
            // sum of elements so far
            sum += arr[j];

            // if sum is seen before, we have found a sub-array
            // with 0 sum
            if (sum == 0) {
                cout << "Subarray [" << i << ".." << j << "]\n";
            }
        }
    }
}
*/
// main function
int main()
{
    int soa, tmp;
    cin>>soa;
    int arr[soa];
    for(unsigned i = 0; i < soa; i++)
    {
       cin>>tmp;
       arr[i] = tmp & 1 ?-1:1;

    }
    int cnt = 0;
    int sum = 0;
    for (int i = 0; i < soa; i++)
    {
        int sum = 0;

        // consider all sub-arrays ending at j
        for (int j = i; j < soa; j++)
        {
            // sum of elements so far
            sum += arr[j];

            // if sum is seen before, we have found a sub-array
            // with 0 sum
            if (sum == 0) {
                cnt ++;
            }
        }
    }
    cout<<cnt;


}