import java.io.*
import java.util.*

fun main(args: Array<String>) {
    solve(System.`in`, System.out)
}

val MAX_N = (1e6 + 10).toInt()
val INF = (1e9 + 7).toInt()
val MOD = (1e9 + 7).toInt()
val INF_F = 1e-6

fun solve(input: InputStream, output: OutputStream) {
    val reader = InputReader(BufferedInputStream(input))
    val writer = PrintWriter(BufferedOutputStream(output))

    solve(reader, writer)
    writer.close()
}

fun solve(reader: InputReader, writer: PrintWriter) {
    val n = reader.nextInt()
    for (i in n downTo 0)
    {
        val c = reader.nextInt()
        c = c % 6
        if (c == 1) || (c == 0)
        {
            writer.println("B")
        }
        else
        {
            writer.println("A")
        }
    }




}



class InputReader(stream: InputStream) {
    private val reader = BufferedReader(InputStreamReader(stream), 32768)
    private var tokenizer: StringTokenizer? = null

    operator fun next(): String {
        while (tokenizer == null || !tokenizer!!.hasMoreTokens()) {
            try {
                tokenizer = StringTokenizer(reader.readLine())
            } catch (e: IOException) {
                throw RuntimeException(e)
            }

        }
        return tokenizer!!.nextToken()
    }

    fun nextInt(): Int {
        return Integer.parseInt(next())
    }

    fun nextLong(): Long {
        return java.lang.Long.parseLong(next())
    }

    fun nextArrayInt(count: Int): IntArray {
        return nextArrayInt(0, count)
    }

    fun nextArrayInt(start: Int, count: Int): IntArray {
        val a = IntArray(start + count)
        for (i in start until start + count) {
            a[i] = nextInt()
        }
        return a
    }

    fun nextArrayLong(count: Int): LongArray {
        val a = LongArray(count)
        for (i in 0 until count) {
            a[i] = nextLong()
        }
        return a
    }
}
