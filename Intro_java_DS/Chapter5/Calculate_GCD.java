import java.util.Scanner;
class Calculate_GCD
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter two positive integer one after another ? ");
        int a = input.nextInt();
        int b = input.nextInt();
        int curr = 2;
        int gcd  = 1;
        while ( curr <= a && curr <= b)
        {
            if( a % curr == 0 && b % curr == 0)
            {
                gcd = curr;
            }
            curr++;
        }
        System.out.println("Gcd of " + a + " and " + b + " is " + gcd);


    }
}