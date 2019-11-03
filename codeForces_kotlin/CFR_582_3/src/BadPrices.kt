fun main()
{
    val nb_test = readLine()!!.toInt()
    repeat(nb_test)
    {
        val lens = readLine()!!.toInt()
        val vals = readLine()!!.split(" ").map{it.toInt()}
        val rval = vals.reversed()
        var mins = Int.MAX_VALUE
        var answer = 0
        for (curr in rval)
        {
            if (curr > mins) answer += 1
            else mins = curr
        }
        println(answer)

    }
}