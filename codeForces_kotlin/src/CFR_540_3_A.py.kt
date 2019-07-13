import kotlin.*

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints

fun main(args: Array<String>)
{
    solve()
}

private fun solve()
{
    var nb_qry = readInt()
    while(nb_qry > 0)
    {
        var (liters, cost_1, cost_2) =  readStrings().map{ it.toLong() }
        println(listOf( (liters * cost_1) , ((liters / 2) * cost_2) + ((liters % 2) * cost_1)  ).min())

        nb_qry -= 1

    }
}