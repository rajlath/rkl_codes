//thanks to ut.Blast
fun main()
{
    val n = readLine()!!.toInt()
    val arr = readLine()!!.split(" ").map{ it.toInt()}
    val (even, odds) = arr.partition { it.rem(2) == 0 }
    if(even.isNotEmpty() and odds.isNotEmpty())
    {
        println(arr.sorted().joinToString(" "))
    }
    else
    {
        println(arr.joinToString(" "))
    }
}