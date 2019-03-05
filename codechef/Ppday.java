import java.util.*;
import java.io.*;
class Ppday
{
    public static void main(String[] Args) throws IOException
    {
        BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
        int lens = Integer.parseInt(bfr.readLine());
        int Acnt, Bcnt;
        String result;
        for(int i = 0; i < lens; i++)
        {
            String current = bfr.readLine();
            Acnt = 0; Bcnt = 0;result = "yes";
            for(int j = 0; j < current.length(); j++)
            {
                if(current.charAt(j) == 'A')
                {
                    Acnt += 1;
                }
                else
                {
                    Bcnt += 1;
                }
                if (j % 2 != 0)
                {
                    if (Acnt != Bcnt)
                    {
                        result = "no";
                        break;
                    }
                }
            }
            System.out.println(result);
        }

    }
}