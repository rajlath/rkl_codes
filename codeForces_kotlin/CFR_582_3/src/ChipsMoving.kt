fun main()
{
    val n = readLine()!!.toInt()
    val vals = readLine()!!.split(" ").map{it.toInt()}
    val evens = vals.count { it % 2 == 0}
    val answer = minOf(evens, n - evens)
    println(answer)

}