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
    var m = readLn()
    var src = IntArray(n)
    for (i in 0 until n)
    {
        src[i] = (m!![i] - '0')
    }
    var maps = readInts()

    for (i in 0 until n)
    {
        var current = maps[src[i] - 1]
        if( current > src[i])
        {
            var should = i
            while(should < n && maps[src[should] - 1] >= src[should])
            {
                src[should] = maps[src[should] - 1]
                should ++
            }
            break
        }
    }
    println(src.joinToString(""))


}