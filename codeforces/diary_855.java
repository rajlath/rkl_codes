import java.util.*;

public class diary_855
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        String newLine = System.getProperty("line.separator");
        int nos = scan.nextInt();
        scan.nextLine();
        HashMap<String, Integer> done = new HashMap<String, Integer>();
        String name = "";
        for(int i=0; i < nos; i++)
        {
            name = scan.nextLine();
            
            if(done.get(name) != null || (done.get(name) == null && done.containsKey(name)))
            {
                System.out.print("YES");
                System.out.print(newLine);
            }
            else
            {
                System.out.print("NO");
                done.put(name, i);
                System.out.print(newLine);
            }
            
        }
        
    }
}
