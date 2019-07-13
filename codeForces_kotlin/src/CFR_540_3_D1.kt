import kotlin.*

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map{ it.toLong() } // list of longs

fun main(args: Array<String>)
{
    solve()
}

fun check(d:Long, cafine: List<Long>, nb_task:Long):Boolean
{
    var done :Long = 0

    cafine.forEachIndexed { i, element ->
        var cur = element - i / d
        if (cur < 0) cur = 0
        done += cur
    }
    return (done >= nb_task)
}


private fun solve()
{
    var (nb_cups, nb_tasks) = readLongs()
    var caffines = readLongs()
    if (caffines.sum() < nb_tasks)
    {
        println(-1)
    }
    else
    {
        var (left, rite) = listOf<Long>(1, nb_cups)
        var mid :Long=  (left + rite) shr 1
        while(left < rite)
        {
            if (check(mid, caffines, nb_tasks)) rite = mid
            else left = mid + 1
            mid = (left + rite) shr 1
        }
        print(left)
    }

}