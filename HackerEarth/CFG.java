
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static void main (String[] args) {
        //code
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
        int n=sc.nextInt();
        int x=sc.nextInt();
        int y=sc.nextInt();int ans=0;
    boolean dp[]=new boolean[n+1];
    dp[0]=false;
    dp[1]=true;
    for(int i=2;i<=n;i++)
    {
        if(i-1>=0&&dp[i-1]==false)dp[i]=true;
        else if(i-x>=0&&dp[i-x]==false)dp[i]=true;
        else if(i-y>=0&&dp[i-y]==false)dp[i]=true;
        else dp[i]=false;


    }

    if(dp[n]==true)
    System.out.println("G");
    else
        System.out.println("N");
        }}
}
