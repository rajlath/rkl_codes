fun intPowe(base:Long, raise:Long):Long
{
    var result :Long = 1
    var exp :Long = raise
    while (raise > 0)
    {
        result *= result
        exp --
    }
    return result
}
fun main()
{
    var ans = 0
    var lasts = listOf(1L)
    var nbOps = readLine()!!.toInt()
    var limit = intPowe(2, 32)
    while (nbOps > 0)
    {
        var curr = readLine()!!.split(" ")
        when (curr[0])
        {
            "add" -> ans += lasts.last().toInt()
            "end" -> lasts.dropLast(1)
            else ->
            {
                var curr = lasts.last() * curr[1].toLong()
                if (curr >= limit) curr = limit
                lasts += curr
            }
        }
        println(lasts)


        nbOps --
    }
    println(ans)
}