class Solution {
public:
    int superEggDrop(int K, int N) {
        long long dp[105][10005];
        for(int i=1;i<=100;i++){
            dp[i][1]=1;
        }
        for(int i=1;i<=10000;i++)
            dp[1][i]=i;
        for(int i=2;i<=100;i++){
            for(int k=2;k<=10000;k++){
                dp[i][k]=dp[i-1][k-1]+dp[i][k-1]+1;
            }
        }
        int i=0;
        while(++i){
            if(dp[K][i]>=N)
                return i;
        }
        return -5;
    }
};