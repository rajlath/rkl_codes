fun main()
{
    val (given, left, rite) = readLine()!!.split(' ').map{ it.toInt()}
    val mins = (1 shl left) + (given - left - 1)
    val maxs = (1 shl rite) - 1 + (1 shl rite - 1) * (given - rite)
    println("$mins $maxs")

}