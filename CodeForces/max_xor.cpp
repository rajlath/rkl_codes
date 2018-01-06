// C++/C program to find maximum xor value of subarray of
// size k
#include<iostream>
using namespace std;

// Returns maximum XOR value of subarray of size k
int maximumXOR(int arr[] , int n , int k)
{
    // Compute XOR value of first subarray of size k
    int current_xor = 0 ;
    for (int i = 0 ; i < k ; i++)
        current_xor  = current_xor ^ arr[i];

    // Traverse rest of the array
    int max_xor = current_xor;
    for (int i = k ; i < n; i++)
    {
        // First remove previous subarray's first
        // element
        current_xor = current_xor ^ arr[i-k];

        // add new element
        current_xor = current_xor ^ arr[i];

        // Update maximum xor value
        max_xor = max(max_xor, current_xor);
    }

    return max_xor;
}

// Driver program
int main()
{
    int arr[] = {1,2,3,4} ;
    int k = 3;
    int n = sizeof(arr)/sizeof(arr[0]);
    cout << "Maximum XOR : " << maximumXOR(arr, n, k);
    return 0;
}
