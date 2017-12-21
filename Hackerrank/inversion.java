import java.lang.reflect.Array;
import java.util.Arrays;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.SplittableRandom;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;


public class inversion {

public static void main(String[] args) {
    OutputStream outputStream = System.out;
    InputStream inputStream = System.in;
    FastReader in = new FastReader(inputStream);
    int H = in.nextInt();
    for (int i = 0; i < H; ++i) {
        int nos = in.nextInt();
        int[] arr = new [nos]int ;
        for(int j= 0; i<nos; ++nos)
        {
            arr[j] = in.nextInt();
        }


    //int[] arr = {6, 9, 1, 14, 8, 12, 3, 2};
    System.out.println(findinversion(arr,0,arr.length-1));
    }
}

public static int findinversion(int[] arr,int beg,int end) {
    if(beg >= end)
        return 0;

    int[] result = new int[end-beg+1];
    int index = 0;
    int mid = (beg+end)/2;
    int count = 0, leftinv,rightinv;
    //System.out.println("...."+beg+"   "+end+"  "+mid);
    leftinv = findinversion(arr, beg, mid);
    rightinv = findinversion(arr, mid+1, end);
    l1:
    for(int i = beg, j = mid+1; i<=mid || j<=end;/*index < result.length;*/ ) {
        if(i>mid) {
            for(;j<=end;j++)
                result[index++]=arr[j];
            break l1;
        }
        if(j>end) {
            for(;i<=mid;i++)
                result[index++]=arr[i];
            break l1;
        }
        if(arr[i] <= arr[j]) {
            result[index++]=arr[i];
            i++;
        } else {
            //System.out.println(arr[i]+"  "+arr[j]);
            System.out.print(arr[i]+" ");
            count = count+ mid-i+1;
            result[index++]=arr[j];
            j++;
        }
    }

    for(int i = 0, j=beg; i< end-beg+1; i++,j++)
        arr[j]= result[i];
    return (count+leftinv+rightinv);
    //System.out.println(Arrays.toString(arr));
}

static class FastReader {
    private InputStream stream;
    private byte[] buf = new byte[8192];
    private int curChar;
    private int pnumChars;
    private FastReader.SpaceCharFilter filter;

    public FastReader(InputStream stream) {
        this.stream = stream;
    }

    private int pread() {
        if (pnumChars == -1) {
            throw new InputMismatchException();
        }
        if (curChar >= pnumChars) {
            curChar = 0;
            try {
                pnumChars = stream.read(buf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (pnumChars <= 0) {
                return -1;
            }
        }
        return buf[curChar++];
    }

    public int nextInt() {
        int c = pread();
        while (isSpaceChar(c))
            c = pread();
        int sgn = 1;
        if (c == '-') {
            sgn = -1;
            c = pread();
        }
        int res = 0;
        do {
            if (c == ',') {
                c = pread();
            }
            if (c < '0' || c > '9') {
                throw new InputMismatchException();
            }
            res *= 10;
            res += c - '0';
            c = pread();
        } while (!isSpaceChar(c));
        return res * sgn;
    }
    private boolean isSpaceChar(int c) {
        if (filter != null) {
            return filter.isSpaceChar(c);
        }
        return isWhitespace(c);
    }

    private static boolean isWhitespace(int c) {
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    private interface SpaceCharFilter {
        public boolean isSpaceChar(int ch);

    }
}

}
