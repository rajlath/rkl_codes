import kotlin.math.sqrt

fun main() {
    val n = readLine()!!.toInt()
    val a = List(n) { readLine()!!.split(" ").map{it.toInt()} }
    val b = List(n) { i ->
        val j = (i + 1) % n
        val k = (i + 2) % n
        sqrt(a[i][j].toLong() * a[i][k] / a[j][k] * 1.0).toInt()
    }
    println(b.joinToString(" "))
}