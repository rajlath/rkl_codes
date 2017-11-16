import java.util.*;
import java.io.*;
class test
{
    public static void main(String arg[])//throws IOException
    {
        Scanner sc=new Scanner(System.in);      
        int t=sc.nextInt();
        while(t>0)
        {
            t--;
            int n=sc.nextInt();//Integer.parseInt(br.readLine());
            int a[]=new int[n];long sum=0;int flag=0;            
            for(int i=0;i<n;i++)
          {
                a[i]=sc.nextInt();
                if(a[i]<=0)
                {
                    sum+=a[i]; //sum of all negatives with 0
                }
                else
                    flag=1;
          }
          
          
          
          if(flag==0)
          {
              System.out.println(sum);
          }
          else
          {
              Arrays.sort(a);int k=0;long s=0;flag=0;int i;
              for( i=n-1;i>=0;i--)
              {
                  if(a[i]>0)
                  {s+=a[i];
                  k++;
                  }
                  else
                  {flag=1;break;}
              }
              long ans=s*k+sum;
              if(flag==1){
                for(int j=i;j>=0  ;j--)
                 {
                    k++;
                    s=s+a[j];
                    long t1=(s)*(k);
                    sum-=a[j];
                    long t2=t1+sum;
                    if(ans<t2)
                    {
                      ans=t2;                    
                    }
                 
                  
                } 
            }
             
              
             System.out.println(ans); 
          }
        }
    }
}
