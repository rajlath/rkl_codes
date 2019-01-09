import java.util.Scanner;
class PrintCalendar
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter year of the calendar in 4 digits :");
        int year  = input.nextInt();
        System.out.print("Enter month number for the calendar :");
        int month = input.nextInt();
        System.out.println(getNumberofDaysSince1800(year, month));

        printMonthTitle(year, month);
        printMonthBody(year, month);

    }


    public static void printMonthTitle(int year, int month)
    {
        System.out.println(" " + getMonthName(month) + " " + year);
        System.out.println("-----------------------------");
        System.out.println(" Sun Mon Tue Wed Thu Fri Sat");
    }

    public static String getMonthName(int month)
    {
        String monthName = "";
            switch (month)
            {
                case 1: monthName = "January"; break;
                case 2: monthName = "February"; break;
                case 3: monthName = "March"; break;
                case 4: monthName = "April"; break;
                case 5: monthName = "May"; break;
                case 6: monthName = "June"; break;
                case 7: monthName = "July"; break;
                case 8: monthName = "August"; break;
                case 9: monthName = "September"; break;
                case 10:monthName = "October"; break;
                case 11:monthName = "November"; break;
                case 12:monthName = "December";
             }

        return monthName;
    }

    public static void printMonthBody(int year, int month)
    {
        int begin       = getStartDay(year, month);
        int daysInMonth = getNumberOfDaysInMonth(year, month);
        int i = 0;
        for (i = 0; i < begin; i ++)
        {
            System.out.print("    ");
        }
        for (i = 1; i <= daysInMonth; i ++)
        {
            System.out.printf("%4d", i);
            if( (i + begin) % 7 == 0)
            {
                System.out.println();
            }
        }

        System.out.println();
    }

    public static int getStartDay(int year, int month)
    {
        int totalDays = getNumberofDaysSince1800(year, month);
        int start_day = (totalDays + 3) % 7;
        return start_day;
    }
    public static int getNumberofDaysSince1800(int year, int month)
    {
        int total_days = 0;
        for (int i = 1800; i <= year; i ++)
        {
            int days =  isLeapYear(i) ? 366 : 365;
            total_days = total_days + days;
        }
        for(int i = 1; i < month; i++)
        {
            total_days  = total_days + getNumberOfDaysInMonth(year, i);

        }
        return total_days;
    }

    public static boolean isLeapYear(int year)
    {
        return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
    }

    public static int getNumberOfDaysInMonth(int year, int month)
    {
        int days = 0;
        switch(month)
        {
            case  1:
            case  3:
            case  5:
            case  7:
            case  8:
            case 10:
            case 12: days =  31; break;
            case  4:
            case  6:
            case  9:
            case 11: days = 30; break;
            case  2: days = isLeapYear(year) ? 29 : 28;
        }
        return days;
    }

}
