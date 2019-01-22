import java.util.*;
public class CFR_532_2_A
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int ar[]=new int[n];
        int min=100,max=0,i,j;
        for(i=0;i<n;i++)
        {
            ar[i]=sc.nextInt();
            max=Math.max(max,ar[i]);
            min=Math.min(min,ar[i]);
        }
        int x=999999999,num=0;
        for(j=min;j<=max;j++)
        {
            int sum=0;
            for(i=0;i<n;i++)
            {
                sum+=Math.min(Math.abs(ar[i]-j),Math.abs(Math.abs(ar[i]-j)-1));
            }
            if(x>sum)
            {
                x=sum;
                num=j;
            }
        }
        System.out.println(num+" "+x);
    }
}