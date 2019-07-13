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
    var n = readInt()
    var valids = mutableSetOf<Int>()
    while (!valids.contains(n))
    {
        valids.add(n)
        n ++
        while(n % 10 == 0) n /= 10
    }
    println(valids.size)

}