import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter
import java.io.StreamTokenizer

var n: Int = 0
var e: Array<IntArray> = emptyArray()
var dp: Array<Array<Array<IntArray>>> = emptyArray()

fun win( u: Int, v: Int, last: Int, turn: Int ): Int {
    if ( dp[u][v][last][turn - 1] > 0 ) return dp[u][v][last][turn - 1]
    var wins = false
    val o = if ( turn == 1 ) u else v
    for ( w in 0 until n ) {
        if ( e[o][w] >= last ) {
            wins = wins or ( win( if ( turn == 1 ) w else u, if ( turn == 1 ) v else w, e[o][w], 3 - turn ) == turn )
        }
    }
    dp[u][v][last][turn - 1] = if ( wins ) turn else 3 - turn
    return dp[u][v][last][turn - 1]
}

fun main(args: Array<String> ) {
    val st = StreamTokenizer( BufferedReader( InputStreamReader( System.`in` ) ) )
    val out = PrintWriter( System.out )
    n = st.nextInt()
    val m = st.nextInt()
    e = Array( n, { IntArray( n, { -1 } ) } )
    for ( i in 1 .. m ) {
        val u = st.nextInt() - 1
        val v = st.nextInt() - 1
        e[u][v] = st.next()[0] - 'a'
    }
    dp = Array( n, { Array( n, { Array( 'z' - 'a' + 1, { IntArray( 2 ) } ) } ) } )
    for ( i in 0 until n ) {
        for ( j in 0 until n ) {
            out.print( if ( win( i, j, 0, 1 ) == 1 ) 'A' else 'B' )
        }
        out.println()
    }
    out.close()
}

fun StreamTokenizer.nextInt(): Int {
    nextToken()
    return nval.toInt()
}

fun StreamTokenizer.next(): String {
    nextToken()
    return sval
}