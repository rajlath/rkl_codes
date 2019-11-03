fun main() {
    fun readInt() = readLine()!!.toInt()
    fun readLong() = readLine()!!.toLong()
    fun readInts() = readLine()!!.split(" ").map(String::toInt)
    fun readLongs() = readLine()!!.split(" ").map(String::toLong)

    val (numMessages, displaySize) = readInts()
    val ids = readInts()
    var pos = 0
    val visible = mutableSetOf<Int>()
    val display = IntArray(displaySize) { -1 }
    for (id in ids) {
        if (id !in visible) {
            visible.remove(display[pos])
            display[pos] = id
            visible.add(id)
            pos = (pos + 1) % displaySize
        }
    }
    pos--
    if (pos < 0) pos = displaySize - 1
    val sb = StringBuilder()
    var elements = 0L
    for (i in pos downTo 0) if (display[i] != -1) {
        sb.append("${display[i]} ")
        elements++
    }
    for (i in displaySize - 1 downTo pos + 1) if (display[i] != -1) {
        elements++
        sb.append("${display[i]} ")
    }
    println(elements)
    print(sb.toString())
}