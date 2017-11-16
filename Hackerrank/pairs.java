/*
#5 2  
#1 5 3 4 2  
*/

import java.util.*;

class pairs
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int noe = scan.nextInt();
        int k   = scan.nextInt();
        
        int[] arr = new int[noe];
        for (int i=0; i < noe; i++)
        {
            arr[i] = scan.nextInt();
        }
        Arrays.sort(arr);
        int pair = 0;
        for (int i=0; i < noe; i++)
        {
            for (int j = i+1; j < noe; j++)
            {
                if (arr[j] - arr[i] == k)
                {
                    pair++;
                    break;
                }
                
            }
        }
        System.out.print(pair);
        
    }
}
