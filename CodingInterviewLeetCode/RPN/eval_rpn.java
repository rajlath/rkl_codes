import java.util.*;

public class eval_rpn
{
    public static void main(String[] args)
    {
        String[] tokens = new String[] { "2" , "1" , "+" , "3" , "*" } ;
        System.out.println( process_equation(tokens) );

    }

    public static int process_equation(String[] tokens)
    {
        int return_value = 0;
        String operators  = "+-*/";
        Stack <String> stack = new Stack<String> ();

        for (String curr : tokens)
        {
            if(! operators.contains(curr) )
            {
                stack.push(curr);
            }
            else
            {
                int a = Integer.valueOf(stack.pop());
                int b = Integer.valueOf(stack.pop());
                switch(curr)
                {
                    case "+"    :
                                stack.push(String.valueOf(a + b));
                                break;
                    case "-"    :
                                stack.push(String.valueOf(a - b));
                                break;
                    case "*"    :
                                stack.push(String.valueOf(a * b));
                                break;
                    case "/"    :
                                stack.push(String.valueOf(a / b));
                }

            }
        }

        return_value = Integer.valueOf(stack.pop());

        return return_value;
    }
}