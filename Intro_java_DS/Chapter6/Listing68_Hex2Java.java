import java.util.Scanner;
class Listing68_Hex2Java
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter a number in Hex : ");
        String hex = input.nextLine();
        System.out.println("Decimal equivalen of " + hex + " is :" + hex2dec(hex.toUpperCase()));
        System.out.println("Print a random char between E and T :" + randomChars('E', 'T'));


    }

    private static int hex2dec(String hex)
    {
        int result = 0;
        for(int i = 0; i < hex.length(); i++)
        {
            result = result * 16 + (hexCharVal(hex.charAt(i)));
        }
        return result;
    }
    private static int hexCharVal(char c)
    {
        if (c >= 'A' && c <= 'F')
        {
            return 10 + c - 'A';
        }
        else
        {
            return c - '0';
        }
    }
    public static char randomChars(char a, char b)
    {
        char result ;
        result =  (char)(a +  Math.random() * (b - a + 1));
        return result;
    }

}
