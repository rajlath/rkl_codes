import kotlin.math.*
fun main() {
    var (n, m) = readLine()!!.split(" ").map { it.toInt() }
    var vals = readLine()!!.split(" ").map { it.toInt() }.sorted()
    var cnts = IntArray(200005, { 0 })
    var answ = IntArray(200005, { 0 })
    for (i in 0 until n) {
        var curr = vals[i]
        var indx = 0
        while (curr > 0) {
            if (cnts[curr] < m) {
                cnts[curr]++
                answ[curr] += indx
            }
            curr /= 2
            indx++

        }

    }
    var result = Int.MAX_VALUE
    for (i in 1..vals[n - 1]) {
        if (cnts[i] == m) result = min(result, answ[i])
    }
    println(result)
}




/*

 */