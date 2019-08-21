fun main() {
    val q = readInt()

    output {
        repeat(q) {
            val (n, k) = readInts()
            val a = readInts()

            val ans = mutableListOf<Int>()

            for(i in a.indices) {
                if(a[i] and 1 == 0) continue

                if(ans.size < k-1) {
                    ans.add(i + 1)
                } else {
                    val rem = (i until a.size).count { a[it] and 1 == 1 }
                    if(rem and 1 == 1) ans.add(n)
                    break
                }
            }

            if(ans.size == k) {
                println("YES")
                println(ans.joinToString(" "))
            } else println("NO")
        }
    }
}

fun readLn() = readLine()!!
fun readInt() = readLn().toInt()
fun readDouble() = readLn().toDouble()
fun readLong() = readLn().toLong()
fun readStrings() = readLn().split(' ')
fun readInts() = readStrings().map { it.toInt() }
fun readDoubles() = readStrings().map { it.toDouble() }
fun readLongs() = readStrings().map { it.toLong() }

class Output {
    private val sb = StringBuilder()
    fun print(o: Any?) { sb.append(o) }
    fun println() { sb.append('\n') }
    fun println(o: Any?) { sb.append(o).append('\n') }
    @JvmName("_print") fun Any?.print() = print(this)
    @JvmName("_println") fun Any?.println() = println(this)
    fun nowPrint() { kotlin.io.print(sb) }
}
inline fun output(block: Output.()->Unit)
{ Output().apply(block).nowPrint() }
