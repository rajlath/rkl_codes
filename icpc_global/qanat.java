import java.util.*;

public class qanat {

    public static double[] dividers;
    public static double[] costs;
    public static double r;

    public static void main(String[] args) {

        // Get input.
        Scanner stdin = new Scanner(System.in);
        int w = stdin.nextInt();
        int h = stdin.nextInt();
        int n = stdin.nextInt();

        // Will store all scaled answers here.
        dividers = new double[0];
        costs = new double[n+1];

        // This is the key value for this triangle.
        r = (double)h/w;

        // We calculate this by bisecting the path of length 1 and length r(vertical).
        costs[0] = (1+r)*(1+r)/4;

        // Iteratively calculate the answer for a higher number of vertical paths.
        for (int k=1; k<=n; k++) {

            double low = 0, high = 1;

            // Do a ternary search since this function goes down and back up.
            while (high-low > 1e-7) {

                double mid = (low+high)/2;

                // Try this spot and a bit past it.
                double lowtry = eval(k, mid);
                double hightry = eval(k, mid+1e-9);

                // Go the appropriate direction.
                if (lowtry > hightry) 	low = mid;
                else					high = mid;
            }

            // It's better to stop the ternary search early and sweep through here.
            double bestMult = low, delta = (high-low)/100;
            double bestVal = eval(k, bestMult);
            for (int i=1; i<=100; i++) {
                double cur = eval(k, low+i*delta);
                if (cur < bestVal) {
                    bestVal = cur;
                    bestMult = low+i*delta;
                }
            }

            // Our answer for k.
            costs[k] = bestVal;

            // Scale all the rest by this factor.
            double[] tmp = new double[k];
            for (int i=0; i<k-1; i++)
                tmp[i] = dividers[i]*bestMult+1e-12;
            tmp[k-1] = bestMult+1e-12;

            // Copy back
            dividers = tmp;
        }

        // This is what they want for output.
        System.out.println(costs[n]*w*w);
        for (int i=0; i<n&&i<10; i++)
            System.out.println(dividers[i]*w);
    }

    // The best cost of using loc as the LAST cut off for k vertical tunnels.
    public static double eval(int k, double loc) {

        // Mid point of last trapezoid.
        double critical = (r*loc + 1 - loc + r)/2;

        // Here it is!
        return costs[k-1]*loc*loc + critical*critical - (loc*r*loc*r)/2;
    }
}