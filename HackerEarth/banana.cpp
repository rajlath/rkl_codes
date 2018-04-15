#include <iostream>
using namespace std;
#include<bits/stdc++.h>
long int Search(long int arr[],long int l,long int r,long int x,long int n);
int main() {
	// your code goes here
		int tt;
	cin>>tt;
	while(tt--)
    {
    long int n,h,i,result;
    cin>>n>>h;
    long  int arr[n];
    for(i=0;i<n;i++)
        cin>>arr[i];
        sort(arr,arr+n);
        if(n==h)
        cout<<arr[n-1]<<endl;
        else
        {
            result=Search(arr,1,arr[n-1],h,n);
            cout<<result<<endl;
        }
    }
	return 0;

}
long int Search(long int arr[],long int l,long int r,long int h,long int n)
{
    if(r>=l)
    {
        long int mid= (l+r)/2; long int i; long int k;
         long int count=0;
         k=mid;
	        for(i=0;i<n;i++)
	        {
	            if(arr[i]%k==0)
	            count+=arr[i]/k;
	            else
	            count+=arr[i]/k+1;
	        }
	         if(l==mid&&r==mid+1)
	             return mid+1;
	        if(count<=h)
	        {

	            return Search(arr,l,mid,h,n);

	        }
	        else
	        {
	            return Search(arr,mid,r,h,n);
	        }

    }
}