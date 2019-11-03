#include<stdio.h>
void f(int n,int arr[n][n],int i,int j)
{
    if(i<0 || j<0 || j>n-1 || i>n-1) return;
    if(arr[i][j]==1)
    {   arr[i][j]=0;
        f(n,arr,i-1,j+1);
        f(n,arr,i-1,j-1);
        f(n,arr,i-1,j);
        f(n,arr,i+1,j+1);
        f(n,arr,i+1,j-1);
        f(n,arr,i+1,j);
        f(n,arr,i,j+1);
        f(n,arr,i,j-1);
    }
    return;
}
int main(){int n;scanf("%d",&n);int arr[n][n];int r,g,b;
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        scanf("%d %d %d",&r,&g,&b);if(g>r+b)arr[i][j]=1;else arr[i][j]=0;
    }
}
int count=0;
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        if(arr[i][j]==1)count++;f(n,arr,i,j);
    }
}
printf("%d\n",count);
    return 0;
}