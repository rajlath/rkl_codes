import java.util.Scanner;


class Exercise5257
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter integer numbers. To stop entering enter 0  ? ");
        int positives = 0;
        int negatives = 0;
        double sums = 0.0;
        int cnts = 0;
        int curr = 0;
        while ( true )
        {
            curr = input.nextInt();
            if (curr == 0) break;
            sums += curr;
            cnts += 1;
            if (curr > 0)
            {
                positives ++;
            }
            else
            {
                negatives ++;
            }
        }
        double avg = sums / cnts ;
        System.out.printf("The number of positives = %d\n", positives);
        System.out.printf("The number of negatives = %d\n", negatives);
        System.out.printf("Total is                = %4.2f\n", sums);
        System.out.printf("Average of the numbers  = %4.2f"  , avg );


    }
}