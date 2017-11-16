/*
5 1 2 3
1 2 3 4 5

*/

import java.util.*;
import java.lang.Math.*;

public class ring_855
{
    public static double max(double a, double b)
    {
        double mx = (a > b) ? a : b;
        return(mx);
    }
    
    public static void main(String[] args)
    {
        String newline = System.getProperty("line.separator");
        Scanner ins = new Scanner(System.in);
        int  n = ins.nextInt();
        long p = ins.nextInt();
        long q = ins.nextInt();
        long r = ins.nextInt();
        
        long a = ins.nextInt();
        long best1 = p * a;
        long best2 = p*a + q*a;
        long best3 = p*a  + q*a + r*a;       
        
        
        for (int i=1; i<n;i++)
        {
            long tmp;
            a = ins.nextInt();
            tmp = p*a;
            if (tmp > best1)
            {
                best1 = tmp;
            }
            tmp = best1 + (q * a);
            if (tmp > best2)
            {
                best2 = tmp;
            }
            tmp = best2 + (r * a);
            if (tmp > best3)
            {
                best3 = tmp;
            }
            
            
            
        }
        
        System.out.print(best3);
        
        
        
    }
    
    
}
