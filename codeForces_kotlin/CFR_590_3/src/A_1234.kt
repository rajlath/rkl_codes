fun main()
{
    val nbQry = readLine()!!.toInt()
    (1..nbQry).forEach {
        var nbs = readLine()!!.toInt()
        val sums = readLine()!!.split(" ").map{it.toInt()}.sum()
        val ods  = if (sums % nbs == 0) 0  else 1

        println(sums / nbs + ods)

    }
}