import kotlin.math.max

fun main() {
    val T = readLine()!!.toInt()
    case@for (i in 1..T) {
        val (n,m,k) = readInts()
        var cur = m
        val h = readInts().toIntArray()
        for (i in 0 until n-1){
            cur += h[i] - maxOf(0,h[i+1]-k)
            if(cur < 0){
                println("NO")
                continue@case
            }
        }
        println("YES")
    }
}

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints