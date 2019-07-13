//Thanks to moss3s
import kotlin.*

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map{ it.toLong() } // list of longs

fun main(args: Array<String>)
{
    var nbTests = readInt()
    while(nbTests > 0)
    {
        var source = readLn()
        var target = readLn()
        var position = 0
        var invalid  = false
        for (chars in target)
        {
            if(source.getOrNull(position) == chars) position ++
            else if ( (chars == '+')
                and (source.getOrNull(position) == '-')
                and (source.getOrNull(position + 1) == '-'))
                position += 2
            else invalid = true

        }
        println(if ((invalid) or (position != source.length)) "NO" else "YES")

        nbTests --
    }

    }