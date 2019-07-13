import kotlin.*

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map{ it.toLong() } // list of longs

fun main(args: Array<String>)
{
    var nbTests = readInt()
    repeat(nbTests)
    {
        var TwoSums = readInts()
        var couldbe1 = 1
        var couldbe2 = TwoSums.min()!! - 1
        var couldbe3 = TwoSums.max()!! - couldbe2
        println("$couldbe1 $couldbe2 $couldbe3")

    }
    /*
    while(nbTests > 0)
    {
        var TwoSums = readInts()
        var couldbe1 = 1
        var couldbe2 = TwoSums.min()!! - 1
        var couldbe3 = TwoSums.max()!! - couldbe2
        println("$couldbe1 $couldbe2 $couldbe3")
        nbTests -= 1
    }
    */


}

