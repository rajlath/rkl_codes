/**
* The class Circular_Matrix creates a Square Matrix of size n*n and fills it in a circular fashion
* @author : www.javaforschool.com
* @Program Type : BlueJ Program - Java
*/

import java.util.*;
class Circular_Matrix
    {
        public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter the number of elements : ");
            int n = sc.nextInt();
            int arr[] = {2, 5, 12, 22, 45, 55, 1, 6, 8};
            int A[][] = new int[n][n];
            int k=0, c1=0, c2=n-1, r1=0, r2=n-1;

            while(k<=n*n+1)
                {
                    for(int i=c1;i<=c2;i++)
                    {
                        if(k>=9) break;
                        A[r1][i]=arr[k++];
                    }

                    for(int j=r1+1;j<=r2;j++)
                    {
                        if(k>=9) break;
                        A[j][c2]=arr[k++];
                    }

                    for(int i=c2-1;i>=c1;i--)
                    {
                        if(k>=9) break;
                        A[r2][i]=arr[k++];
                    }

                    for(int j=r2-1;j>=r1+1;j--)
                    {
                        if(k>=9) break;
                        A[j][c1]=arr[k++];
                    }
                    if(k>=9) break;
                 c1++;
                 c2--;
                 r1++;
                 r2--;
                }

            /* Printing the Circular matrix */
            System.out.println("The Circular Matrix is:");
            for(int i=0;i<n;i++)
                {
                    for(int j=0;j<n;j++)
                        {
                            System.out.print(A[i][j]+ "\t");
                        }
                 System.out.println();
                }
        }
    }
