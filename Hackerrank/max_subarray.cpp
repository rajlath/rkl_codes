import java.lang.reflect.Array;
import java.util.Arrays;


public class main {

public static void main(String[] args) {
    int[] arr = {6, 9, 1, 14, 8, 12, 3, 2};
    System.out.println(findinversion(arr,0,arr.length-1));
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
            System.out.println(arr[i]+"  "+arr[j]);
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

}
share