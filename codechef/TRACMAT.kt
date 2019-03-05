import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter
import java.io.StreamTokenizer
import java.util.Arrays;
import java.util.*;

private fun StreamTokenizer.nextInt(): Int {
    nextToken()
    return nval.toInt();
}



fun main( args: Arrays<String>)
{
    val st = StreamTokenizer( BufferedReader( InputStreamReader( System.`in` ) ) );
    var matrix :Arrays = arraysOf<Arrays<Int>>();
    val dims   = st.nextInt();
    for(i in 0..dims)
    {
        var array = arrayOf<Int>(dims);
        for(j in 0..dims)
        {
            array += st.nextInt();
        }
        matrix += array;
    }


}