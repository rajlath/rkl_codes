class BlockDemo
{
    public static void main(String[] args)
    {
        int a, b, c;

        a = 2;
        b = 10;


        if (a < 0)
        {
            System.out.println("a contains a value greater then 0.");
            c = b / a;
            System.out.println("b when divided by a results in :" + c);
        }


        c = b / 4;
        System.out.println("b when divided by 4 results in :"+ c);
    }
}