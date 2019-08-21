fun main() {
    val n = readInt()
    val a = readLine()!!
    val t = intArrayOf(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    a.forEach {
        if (it == 'L') {
            val i = t.indexOfFirst { it == 0 }
            t[i] = 1
        } else if (it == 'R') {
            val i = t.indexOfLast { it == 0 }
            t[i] = 1
        } else {
            t[it.toString().toInt()] = 0
        }
    }
    println(t.joinToString(""))
}

private fun readInt() = readLine()!!.toInt()