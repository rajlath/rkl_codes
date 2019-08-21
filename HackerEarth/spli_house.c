#include<stdio.h>
int main(){
    int n,flag=0;
    scanf("%d",&n);
    char arr[n+1];
    scanf("%s",arr);
    for(int i=1;arr[i]!='\0';i++)
    {
        if(arr[i]=='H'&&arr[i-1]=='H'){
            flag = 1;
        }
        else if(arr[i]=='.')
            arr[i] = 'B';
    }
    if(arr[0]=='.')
        arr[0] = 'B';
    if(flag == 1)
        printf("NO");
    else{
        printf("YES\n");
        for(int i=0;arr[i]!='\0';i++)
            printf("%c",arr[i]);
    }
    return 0;
}