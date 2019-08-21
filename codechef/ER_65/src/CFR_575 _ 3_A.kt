fun main()
{
    val n = readLine()?.toInt() ?:0
    for (i in 1..n)
    {
        val sums = readLine()!!.split(" ").map { it.toLong()}.sortedBy { it }.sum()
        var answ = sums / 2
        println(answ)


    }
}