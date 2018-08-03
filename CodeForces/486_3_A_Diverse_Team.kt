fun readInts(delimit: Char =' ') = readLine()!!.split(delimit).map(String::toInt)

fun main(args:Array<String>)
{
    var (n,k) = readInts()
    var arr   = readInts()

    var distinct = listOf<Int>()
    var indexs   = listOf<Int>()
    var ans      = "NO"
    for (i in arr.indices)
    {
        var curr = arr[i]
        if (curr in distinct)
        {
            continue
        }
        else
        {
            distinct += curr
            indexs += (i+1)
            if (distinct.size == k)
            {
                ans = "YES"
                break
            }

        }
    }
    println(ans)
    if (ans == "YES") println(indexs.joinToString(" "))
}
