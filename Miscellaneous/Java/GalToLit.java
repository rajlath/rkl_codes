class GalToLit
{
    public static void main(String[] args)
    {
        double gallons, liters ;
        int counter;
        counter = 0;

        for(gallons=1.0; gallons < 101.0; gallons++ )
        {
            liters = gallons * 3.8754;
            System.out.println(gallons +" gallon is equivalent to :" + liters + " liters.");
            counter++;
            if (counter == 10)
            {
                System.out.println();
                counter = 0;
            }
        }



    }
}