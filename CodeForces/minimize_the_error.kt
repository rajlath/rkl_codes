fun main(args: Array<String>) {
    val (n ,k1, k2) = readLine()!!.split(' ').map { it.toInt() }
    val a = readLine()!!.split(' ').map { it.toLong() }
    val b = readLine()!!.split(' ').map { it.toLong() }

    val d = List(a.size, {Math.abs(b[it] - a[it])}).toMutableList()

    (1 .. k1 + k2).forEach {
        d.sortDescending()
        d[0] = Math.abs(d[0] - 1)
        println(d)
    }


    println(d.map { it * it }.sum())
}

fun List<Long>.sortMax():Int {
    for (i in 1 until this.size){
        if (this[i] < this[i-1]){
            return i-1
        }
    }
    return this.size-1
}