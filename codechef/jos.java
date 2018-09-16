import java.lang.*
import java.io.Console;;

public class jos{
    int valueOfL = 5 - Integer.highestOneBit(5);
    int safePosition = 2 * valueOfL + 1;
    System.out.println(safePosition);
}