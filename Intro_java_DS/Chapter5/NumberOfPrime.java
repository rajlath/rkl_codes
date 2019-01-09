import java.util.Scanner;
class NumberOfPrime
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number of primes to be displayed  ? ");
        final int NO_OF_PRIMES = input.nextInt();
        System.out.println("Enter number of primes each row will contain ? ");
        final int NO_OF_COLUMNS = input.nextInt();

        int done = 0;
        int curr = 2;

        while (done < NO_OF_PRIMES)
        {
            boolean isPrime = true;
            for(int divisor = 2; divisor <= curr/2; divisor ++)
            {
                if(curr % divisor == 0)
                {
                    isPrime = false;
                    break;
                }
            }
            if(isPrime)
            {
                done ++;
                if(done % NO_OF_COLUMNS == 0)
                {
                    System.out.println(curr);
                }
                else
                {
                    System.out.print(curr + " ");
                }

            }
            curr ++;

        }

    }
}