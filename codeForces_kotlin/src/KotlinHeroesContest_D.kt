//Thanks to majk
import kotlin.*

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map{ it.toLong() } // list of longs

fun main(args: Array<String>)
{

    val lens = readInt()
    val elements = readInts()
    val minusOnes = elements.count { it == -1}
    val willBe   =  Array(minusOnes) { mutableListOf<Int>() }
    var E = mutableListOf<Int>()
    repeat(minusOnes) { E.add(it)}
    //println(E)
    var i = 0
    while ( i < lens )
    {
        val F = mutableListOf<Int>()
        E.forEach{
            if (elements[i] != -1)
            {
                willBe[it].add(elements[i])
                F.add(it)

            }
            i ++
        }
        E = F
    }
    println(minusOnes)
    willBe.forEach {
        println("${it.size} ${it.joinToString(" ") {it.toString() } }")
    }


}