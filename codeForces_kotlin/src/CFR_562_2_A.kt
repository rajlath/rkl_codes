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
    var(nb_st, sta, ena, stb, enb) = readInts()
    var a = sta
    var b = stb
    var ans = "NO"
    while(a != ena && b != enb)
    {
        a ++
        b --
        if (a > nb_st) a = 1
        if (b < 1) b = nb_st
        if (a == b)
        {
            ans = "YES"
            break
        }

    }
    println(ans)
}