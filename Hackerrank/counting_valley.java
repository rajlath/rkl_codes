import java.io.*;
import java.util.*;

public class counting_valley
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.nextLine();
        String ops = input.nextLine();
        
        int level = 0;
        int valley = 0;
        boolean belowSea = false;
        
        for(int i=0; i < n; i++)
        {
            char op = ops.charAt(i);
            if (op == 'D')
            {
                level++;
            }
            else
            {
                level--;
            }
            if(!belowSea && level <= 0)
            {
                valley++;
                belowSea = true;  
            }
            if (level >= 0)
            {
                belowSea = false ; 
            }
        }
        
        System.out.println(valley);
        
        
    }
}

