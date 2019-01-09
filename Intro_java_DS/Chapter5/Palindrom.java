import java.util.Scanner;
class Palindrom
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a string  ? ");
        String src = input.nextLine();
        int left, rite;
        left = 0;
        rite = src.length() - 1;
        Boolean isPalindrome = true;
        while (left < rite)
        {
            if (src.charAt(left) != (src.charAt(rite)))
            {
                System.out.println(src + " is not a palindrome.");
                isPalindrome = false;
                break;
            }
            left ++;
            rite --;
        }
        if (isPalindrome)
        {
            System.out.println(src + " is a valid palindrome.");
        }

    }
}