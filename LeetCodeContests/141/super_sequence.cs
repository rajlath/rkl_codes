public class Solution {
    public string ShortestCommonSupersequence(string str1, string str2) {
        string a = str1;
        string b = str2;
        int m = a.Length, n = b.Length;
        int[,] dp = new int[m+1,n+1];
        for (int i = 0; i <= m; i++)
        {
            for (int j = 0; j <= n; j++)
            {
               if (i == 0)
                   dp[i,j] = j;
               else if (j == 0 )
                   dp[i,j] = i;
               else if (a[i-1] == b[j-1])
                    dp[i,j] = 1 + dp[i-1,j-1];
               else
                    dp[i,j] = 1 + Math.Min(dp[i-1,j], dp[i,j-1]);
            }
        }


       string res = "";
       int k = m, l = n;
       while (k > 0 && l > 0)
       {

          if (a[k-1] == b[l-1])
          {
              res = a[k-1] + res;
              k--;
              l--;
          }


          else if (dp[k-1,l] < dp[k,l-1])
          {
              res = a[k-1] + res;
              k--;
          }
          else
          {
              res = b[l-1] + res;
              l--;
          }
       }


       while (k > 0)
       {
           res = a[k-1] + res;
           k--;
       }

       // Copy remaining characters of string 'b'
       while (l > 0)
       {
           res = b[l-1] + res;
           l--;
       }

       // Print the result
       return res;

    }
}
