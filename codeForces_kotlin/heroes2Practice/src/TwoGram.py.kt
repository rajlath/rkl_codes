

fun main()
{
    val len = readLine()!!.toInt()
    var given = readLine()!!.trim()
    var ngrams: MutableMap<String, Int> = mutableMapOf()

    for (i in 0..len - 2)
    {
        var curr = given.substring(i,i+2)
        ngrams[curr] = ngrams.getOrDefault(curr, 0) + 1

    }

    var result = ""
    var maxs = 0
    for ((k, v) in ngrams)
    {
        if (v > maxs)
        {
            result = k
            maxs = v
        }

    }
    println(result)
}