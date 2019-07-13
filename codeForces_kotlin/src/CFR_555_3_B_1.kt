import kotlin.*;

fun main(args: Array<String>) {
    var n = readLine()!!.toInt()
    var s = readLine()
    var num = IntArray(n)
    for (i in 0 until n) {
        num[i] = (s!![i] - '0')
    }
    var ar = readLine()!!.split(" ").map { it.toInt() }
    for (i in 0 until n) {
        var change = ar[num[i] - 1]
        if (change > num[i]) {
            var j = i
            while (j < n && ar[num[j] - 1] >= num[j]) {
                num[j] = ar[num[j] - 1]
                j++
            }
            break
        }
    }
    print(num.joinToString(""))
}