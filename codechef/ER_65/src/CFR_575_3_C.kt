import kotlin.math.max
import kotlin.math.min

const val INF = 100000
fun main()
{
    val q = readInt()
    repeat(q)
    {
        val n = readInt()
        var l = -INF
        var r = +INF
        var u = +INF
        var d = -INF
        repeat(n)
        {
            val args = readInts().iterator()
            val x  = args.next()
            val y  = args.next()
            val f1 = args.next()
            val f2 = args.next()
            val f3 = args.next()
            val f4 = args.next()

            if (f1 == 0) l = max(x, l)
            if (f2 == 0) u = min(y, u)
            if (f3 == 0) r = min(x, r)
            if (f4 == 0) d = max(y, d)

            if ((l > r) or (d > u))
            {
                println(0)
            }
            else
            {
                println("1  ${(l + r)/2} ${(u + d)/2}")
            }

        }


    }




    fun readLn() = readLine()!!
    fun readInt() = readLn().toInt()
    fun readDouble() = readLn().toDouble()
    fun readLong() = readLn().toLong()
    fun readStrings() = readLn().split(' ')
    fun readInts() = readStrings().map { it.toInt() }
    fun readDoubles() = readStrings().map { it.toDouble() }
    fun readLongs() = readStrings().map { it.toLong() }
}