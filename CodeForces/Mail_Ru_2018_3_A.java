import java.util.*;
public class Mail_Ru_2018_3_A
{
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        int[] arr = new int[101];
        int n = sc.nextInt();
        for(int i = 1; i <= n; i++)
        {
            int nbElement = sc.nextInt();
            for (int j = 1; j <= nbElement; j++)
            {
                arr[sc.nextInt()]++;

            }

        }
        for (int i = 1; i <= 100; i++)
        {
            if (arr[i] == n) System.out.print(i + " ");
        }
    }
}
