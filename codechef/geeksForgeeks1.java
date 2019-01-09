// Java program to find x such that
// X + sumOfDigits(X) = N
import java.util.*;
import java.lang.*;
import java.io.*;

class GeeksforGeeks1 {

    // Computing the sum of digits of x
    static int sumOfDigits(long x)
    {
        int sum = 0;
        while (x > 0) {
            sum += (x % 10);
            x /= 10;
        }
        return sum;
    }

    // Checks for 100 numbers on both left
    // and right side of the given number to
    // find such numbers X such that
    // X + sumOfDigits(X) = N and prints solution.
    static void compute(long n)
    {
        long answer[] = new long[100];
        int pos = 0;

        // Checking for all possibilities of the answer
        // in the given range
        for (int i = 0; i <= 100; i++) {

            // Evaluating the value on the left side of the
            // given number
            long valueOnLeft = Math.abs(n - i) +
                            sumOfDigits(Math.abs(n - i));

            // Evaluating the value on the right side of the
            // given number
            long valueOnRight = (n + i) + sumOfDigits(n + i);

            if (valueOnRight == n)
                answer[pos++] = (n + i);
            if (valueOnLeft == n)
                answer[pos++] = Math.abs(n - i);
        }

        if (pos == 0)
            System.out.print(-1);
        else
            for (int i = 0; i < pos; i++)
                System.out.println("X = " + answer[i]);
    }
    // Driver Function
    public static void main(String[] args)
    {
        long N = 100;
        compute(N);
    }
}
