class IfDemo
{
    public static void main(String[] args)
    {
        int a, b, c ;

        a = 2;
        b = 3;

        if (a == b){ System.out.println("a is equal to b."); }
        if (a <  b){ System.out.println("a is less  then b."); }
        if (a >  b){ System.out.println("a is more then b."); }

        c =  b - a;

        if (c >= 0){ System.out.println("c is a positive number."); }
        if (c <  0){ System.out.println("c is a negative number."); }

        if (a == c){ System.out.println("a is equal to c."); }
        if (a < c){ System.out.println("a is less  then c."); }
        if (a > c){ System.out.println("a is more then c."); }






    }
}