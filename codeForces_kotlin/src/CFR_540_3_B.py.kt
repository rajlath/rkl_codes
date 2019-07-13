import kotlin.*

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map{ it.toLong() } // list of longs

fun main(args: Array<String>)
{
    solve()
}

private fun solve()
{
    var candies = readInt()
    var weights = readInts()
    var odd_even = mutableListOf<Int>(0, 0)
    var ans = 0
    for(i in 0..candies - 1) odd_even[i%2] += weights[i]
    odd_even[0] -= weights[0]
    if (odd_even[0] == odd_even[1]) ans ++
    for(i in 1..candies - 1)
    {
        odd_even[i%2] += weights[i - 1]
        odd_even[i%2] -= weights[i]
        if (odd_even[0] == odd_even[1]) ans ++
    }
    println(ans)






}