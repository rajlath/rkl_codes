#include <bits/stdc++.h>
using namespace std;


const int N = 100000;               // limit for array size
int n;                              // array size
int tree[2 * N];                    // Max size of tree

// function to build the tree
void build( int arr[])
{

    for (int i=0; i<n; i++)         // insert leaf nodes in tree
        tree[n+i] = arr[i];

    // build the tree by calculating parents
    for (int i = n - 1; i > 0; --i)
        tree[i] = tree[i<<1] + tree[i<<1 | 1];
}

// function to update a tree node
void updateTreeNode(int p, int value)
{

    tree[p+n] = value;               // set value at position p
    p = p+n;

    // move upward and update parents
    for (int i=p; i > 1; i >>= 1)
        tree[i>>1] = tree[i] + tree[i^1];
}

// function to get sum on interval [l, r)
int query(int l, int r)
{
    int res = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1)        // loop to find the sum in the range
    {
        if (l&1)
            res += tree[l++];

        if (r&1)
            res += tree[--r];
    }

    return res;
}

// driver program to test the above function
int main()
{
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};


    n = sizeof(a)/sizeof(a[0]);                    // n is global
    build(a);                                      // build tree
    cout << query(1, 3)<<endl;                     // print the sum in range(1,2) index-based
    updateTreeNode(2, 1);                          // modify element at 2nd index
    cout << query(1, 3)<<endl;                     // print the sum in range(1,2) index-based

    return 0;
}