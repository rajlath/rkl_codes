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
    var lens = readInt()
    var elem = readInts()
    var left = 0
    var rite = lens - 1
    var rets = ""
    var last = -1
    while (left < rite) {
        if ((elem[left] > last) && ((elem[rite] >= elem[left]) || (elem[rite] <= last))) {
            last = elem[left]
            rets += "L"
            left += 1
        } else if ((elem[rite] > last) && ((elem[left] >= elem[rite]) || (elem[left] <= last))) {
            last = elem[rite]
            rets += "R"
            rite -= 1

        } else break
    }
    println(rets.length)
    println(rets)
}

