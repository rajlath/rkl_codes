import java.util.*;
import java.lang.Math.*;
public class TRACMAT
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int nb_test = sc.nextInt();
        while (nb_test-- > 0)
        {
            int dims = sc.nextInt();
            int matrix[][] = new int[dims][dims];
            for(int i = 0; i < dims; i++)
            {
                for(int j = 0; j < dims; j++ )
                {
                    matrix[i][j] = sc.nextInt();
                }
            }

            int maxs = 0;
            for(int i = 0; i < dims-1; i++)
            {
                for(int j = 0; j < dims-1; j++)
                {
                    maxs = java.lang.Math.max(maxs, matrix[i][j] + matrix[i+1][j+1]);
                }
            }
            System.out.println(maxs);
        }


    }
}