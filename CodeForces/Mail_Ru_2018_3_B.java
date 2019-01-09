import java.util.*;
public class Mail_Ru_2018_3_B {
    public static int n, m;
    public static int[][] mods;
    public static long res;
    public static Scanner sc = new Scanner (System.in);
    public static void main(String[] args) {
        n = sc.nextInt();
        m = sc.nextInt();
        mods = new int[m][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                mods[i][j] = (i*i+j*j)%m;
                if (mods[i][j] == 0) calc(i, j);
            }
        }
        System.out.print(res);
    }

    public static void calc(int i, int j) {
        int x = n/m;
        int y = n/m;
        if (i != 0 && n - n%m + i <= n) x++;
        if (j != 0 && n - n%m + j <= n) y++;
        res += (long) x*y;
    }

}