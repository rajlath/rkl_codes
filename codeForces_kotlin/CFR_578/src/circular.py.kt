import kotlin.math.abs

fun main() {
    val args = readStrings().iterator()
    val n = args.next().toLong()
    val m = args.next().toLong()
    val q = args.next().toInt()

    val gcd = n.gcd(m)

    fun subSect(x: Long, y: Long): Long {
        val sn = if(x == 1L) n else m

        return (y-1) / (sn / gcd)
    }

    repeat(q) {
        val (sx, sy, ex, ey) = readLongs()

        if(subSect(sx, sy) == subSect(ex, ey)) println("YES") else println("NO")
    }
}

tailrec fun Long.gcd(b: Long): Long = if(b == 0L) this else b.gcd(this % b)

fun readLn() = readLine()!!
fun readInt() = readLn().toInt()
fun readDouble() = readLn().toDouble()
fun readLong() = readLn().toLong()
fun readStrings() = readLn().split(' ')
fun readStringSeq() = readLn().splitToSequence(' ')
fun readInts() = readStrings().map { it.toInt() }
fun readIntSeq() = readStringSeq().map { it.toInt() }
fun readDoubles() = readStrings().map { it.toDouble() }
fun readDoubleSeq() = readStringSeq().map { it.toDouble() }
fun readLongs() = readStrings().map { it.toLong() }
fun readLongSeq() = readStringSeq().map { it.toLong() }
