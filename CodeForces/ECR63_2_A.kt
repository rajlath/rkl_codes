fun main(args: Array<String>) {
    solve()
}

private fun read(delimit: Char = ' ') = readLine()!!.split(delimit)

private fun solve() {
    read()
    var s = read()[0]

    var idx = 0
    val length = s.length - 1
    var found = false

    while (idx < length) {
        var s1: String = s[idx] + "" + s[idx + 1]
        if (s1 > s1.reversed()) {
            found = true
            break
        }
        idx++
    }

    if (!found) {
        println("NO")
    } else {
        println("YES")
        println("${idx + 1} ${idx + 2}")
    }
}
