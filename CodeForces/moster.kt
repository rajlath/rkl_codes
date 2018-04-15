import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args: Array<String> ) {
    val br = BufferedReader( InputStreamReader( System.`in` ) )
    val s = br.readLine().toCharArray()
    var res = 0
    for ( l in 0 until s.lastIndex ) {
        var from = 0
        var to = 0
        for ( r in l until s.size ) {
            if ( s[r] == ')' ) {
                from --
                to --
            } else if ( s[r] == '(' ) {
                from ++
                to ++
            } else {
                from --
                to ++
            }
            if ( to < 0 ) break
            if ( from < 0 ) from += 2
            if ( from == 0 ) res ++
        }
    }
    println( res )
}