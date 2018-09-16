'''
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sample;
import java.util.*;
/**
 *
 * @author HARSHITH
 */
public class CountN {

    int n,sum;
    public CountN()
    {
        System.out.println("Enterd sum");
        Scanner in=new Scanner(System.in);
        n=in.nextInt();
        sum=in.nextInt();
    }

    int f_DP(int d,int s,int dp[][])
    {
        int ans=0;

        if(dp[d][s]!=-1)
        {
            return dp[d][s];
        }

        for(int i=0;i<=9;++i)
        {             if(s-i>=0) ans+=f_DP(d-1,s-i,dp);
        }

        dp[d][s]=ans;
        return ans;
    }

    int startf_DP()
    {
        int ans=0,i=0,j=0;
        int dp[][]=new int[n+1][sum+1];

        for(i=0;i<=n;++i)
        {
            for(j=0;j<=sum;++j)
            {
                if(i==1 && j<=9)
                {
                    dp[i][j]=1;
                }
                else dp[i][j]=-1;
            }
        }



        for(i=1;i<=9;++i)
        {            if(sum-i>=0) ans+=f_DP(n-1,sum-i,dp);
        }
        System.out.println(ans);
        return ans;
    }



    public static void main(String args[])
    {
        CountN cn=new CountN();
        cn.startf_DP();
    }



}
'''
def FDP(d, s):
    global dp
    ans = 0
    if dp[d][s] != -1:return dp[d][s]
    for i in range(1, 10):
        if s - i >= 0:
            ans += FDP(d-1, s-i)
    dp[d][s] = ans
    return ans

def startFDP(n, sums):
    global dp
    ans, i, j = 0, 0, 0
    dp = [[0 for x in range(sums + 1)] for y in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, sums+1):
            if i == 1 and j <= 9:
                dp[i][j] = 1
            else:
                dp[i][j] = -1
    for i in range(1, 10):
        if sums - i >= 0:
            ans += FDP(n-1, sums-i)
    print(ans)


startFDP(2230, 6)




