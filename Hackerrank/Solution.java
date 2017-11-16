import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int ans = a;
            int cnt = 0;
            for (int x =0; x < n; x++)
            {
                ans = ans + (int)Math.pow((double)2, (double)x) * b ;
                System.out.print(Integer.toString(ans)+" ");
                cnt++;
                if(cnt == 10 && x != n-1)
                {
                    System.out.print("\n");
                    cnt = 0;
                }
                    
            }
            System.out.println();
            
        }
        in.close();
    }
}
