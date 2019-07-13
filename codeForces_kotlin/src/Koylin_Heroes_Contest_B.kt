import kotlin.*

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map{ it.toLong() } // list of longs

fun main(args:Array<String>)
{
    readInt() // this value is not required
    var values = readInts()
    //declare and intialize last two max values
    var maxs   = mutableListOf<Int>(0, 0)
    var valids = 0
    for(vals in values)
    {
        var lowerMax = maxs.min()!!
        if (vals < lowerMax)
        {
            valids+= 1
        }
        else
        {
            // replace lowerMax with current value
            maxs[maxs.indexOf(lowerMax)] = vals
        }
    }
    println(valids)

}