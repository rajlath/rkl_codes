'''
# returns true if there is triplet
# with sum equal to 'sum' present
# in A[]. Also, prints the triplet
def find3Numbers(A, arr_size, sum):

    # Sort the elements
    A.sort()

    # Now fix the first element
    # one by one and find the
    # other two elements
    for i in range(0, arr_size-2):


        # To find the other two elements,
        # start two index variables from
        # two corners of the array and
        # move them toward each other

        # index of the first element
        # in the remaining elements
        l = i + 1

        # index of the last element
        r = arr_size-1
        while (l < r):

            if( A[i] + A[l] + A[r] == sum):
                print("Triplet is", A[i],
                     ',', A[l], ',', A[r]);
                return True

            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else: # A[i] + A[l] + A[r] > sum
                r -= 1

    # If we reach here, then
    # no triplet was found
    return False

Examples
inputCopy
5
2 4 5 4 10
40 30 20 10 40
outputCopy
90
inputCopy
3
100 101 100
2 4 5
outputCopy
-1
inputCopy
10
1 2 3 4 5 6 7 8 9 10
10 13 11 14 15 12 13 13 18 13
outputCopy
33
#include<bits/stdc++.h>
using namespace std;
int n,s[3005],c[3005],r[3005],ans=1e9;
int main()
{
	cin>>n;
	for(int i=1;i<=n;i++)cin>>s[i];
	for(int i=1;i<=n;i++)cin>>c[i];
	for(int i=1;i<=n;i++)
	{
		r[i]=1e9;
		for(int j=i+1;j<=n;j++)
		if(s[i]<s[j])r[i]=min(r[i],c[j]);
	}
	for(int i=1;i<n-1;i++)
	for(int j=i+1;j<n;j++)
	if(s[i]<s[j]&&r[j]<1e9)
	ans=min(ans,c[i]+c[j]+r[j]);
	if(ans<1e9)cout<<ans;else printf("-1");
}
'''
import math
maxv = int(10e18)
noe = int(input())
fs  = [int(x) for x in input().split()]
cost= [int(x) for x in input().split()]
ans = maxv
for i in range(noe):
    l = maxv
    r = maxv
    for j in range(i+1, noe):
        if fs[i] < fs[j]:
            r = min(r, cost[j])
    for j in range(i-1, -1, -1):
        if fs[j] < fs[i]:
            l = min(l, cost[j])
    if l != maxv and r != maxv:
        ans = min(ans, cost[i] + r + l)

print([ans, -1][ans==maxv])





