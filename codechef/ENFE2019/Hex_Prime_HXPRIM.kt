import java.io.ByteArrayInputStream
import java.io.InputStream
import java.util.*

fun main(args: Array<String>) {
    try {
        B1106().run()
    } catch (e: Throwable) {
        println("")
        e.printStackTrace()
    }
}

class B1106 {
    fun run() {
        val sc = Scanner(systemIn())
        val n=sc.nextInt()
        val a=(1..n).map { sc.nextInt() }.sorted()


        var ans=0L
        for(i in 0..(n/2-1)) {
            val s=a[i]+a[a.size-1-i]
            //log("$a $i $s")
            ans+=(s*s)
        }
        println("$ans")
    }

    companion object {
        var inputStr: String? = null

        fun systemIn(): InputStream {
            if (inputStr != null)
                return ByteArrayInputStream(inputStr!!.toByteArray())
            else
                return System.`in`
        }

        var printLog = false
        fun log(str: String) {
            if (printLog)
                println(str)
        }
    }
}