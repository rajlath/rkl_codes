import java.util.*

fun main(args:Array<String>)
{
    var n = readLine()!!.toInt()
    var cnt = 0
    var x = 0
    var y = 0
    for (i in 1 .. n+1)
    {
        for (j in y .. i+1)
        {
            x = i xor j
            if ((x<=j) && (x<=n) && ((x+j ) > i)) cnt += 1
            println(cnt)

        }
    }
    println(cnt)
}
