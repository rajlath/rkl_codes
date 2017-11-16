#copied
/*  
    This is brute force solution of problem in which n numbers are given 10e-6<=a[i]<=10e+6
    Then k queries are given and a number is given in each query ...you have to find whether number 
    exists in array.
 
    Sunil has made solution using binary search
    Kartikay has made using hashing.
 
*/
 
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
 
int main(){
 
     int t;
     scanf("%d",&t);
 
     while(t--){
 
         int n;
          
         scanf("%d",&n);
 
         int arr[1000000],i,j;
 
         for(i=0;i<n;++i){
 
              scanf("%d",&arr[i]);   
 
         }
 
         int k,x,q;
 
         scanf("%d",&q);
 
         for(i=0;i<q;++i){
 
             scanf("%d",&x);
 
             int flag=0;
 
             for(j=0;j<n;++j){
                   
                  if(arr[j]==x){
                      
                       flag=1;
                       break;
                  }
             } 	
 
             if(flag==1)
             	printf("Yes\n");
 
             else
             	printf("No\n");
 
         }
 
     }
 
	 return 0;
}
