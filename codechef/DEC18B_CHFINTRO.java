import java.util.Scanner;
class DEC18B_CHFINTRO
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int nbStudent, checkMmark, curr;
        nbStudent = input.nextInt();
        checkMmark= input.nextInt();
        for( int i =0; i < nbStudent; i++)
        {
            curr = input.nextInt();
            if (curr >= checkMmark)
            {
                System.out.println("Good boi");
            }
            else
            {
                System.out.println("Bad boi");
            }

        }
        input.close();


    }
}