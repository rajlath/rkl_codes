fun main(args: Array<String>) {
    val t = readLine()!!.trim().toInt()
    (1..t).forEach {
        val n = readLine()!!.trim().toInt()
        val x = readLine()!!.trim().split(' ')
            .map{ it.toInt() }
            .zipWithNext{ a, b -> ( n + a - b ) % n }
            .groupingBy{ it }
            .eachCount()

        println( if ( n == 1 || x[ 1 ] == n - 1 || x[ n - 1 ] == n - 1 ) "YES" else "NO" )
    }
}
