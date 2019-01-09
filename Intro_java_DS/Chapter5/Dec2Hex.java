import java.util.Scanner;
class Dec2Hex
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a decimal number  ? ");
        int ins = input.nextInt();
        int dec = ins;
        String hex = "";
        while (dec > 0)
        {
            int curr = dec % 16;
            char hexDigit = (curr >= 0 && curr <= 9) ? (char) (curr + '0') : (char)(curr % 10 + 'A' );
            hex = hexDigit + hex;
            dec /= 16;
        }
        System.out.println("Hex value of  " + ins + " is " + hex);


    }
}