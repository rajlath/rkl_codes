import kotlin.collections.ArrayList
fun main()
{
    val lens = readLine()!!.toInt()
    var vals = readLine()!!.split(" ").map{it.toLong()}
    val d = Array<ArrayList<Long>>(40) { ArrayList() }
    for(i in 0..lens - 1)
    {
        var v = vals[i]
        var a = 0
        while (v % 3 == 0L )
        {
            a ++
            v /= 3

        }
        d[a].add(vals[i])
    }
    for (i in 39 downTo 0)
    {
        for (j in d[i].sorted())
        {
            print("$j ")
        }
    }

}