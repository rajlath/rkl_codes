import kotlin.math.*
var ones = LongArray(18, { 0L })
fun main() {


    for (i in 1..17)
    {
        ones[i] = ones[i - 1] * 10 + 1
    }
    var n = readLine()!!.toLong()
    println(dfs(n, 16))

}

fun dfs(n:Long, i:Int):Long
{
    var n1 = n
   var k = n1 / ones[i]
    n1 %= ones[i]
    if(n1 == 0L)
    {
        return k * i
    }
    else
    {
        return k*i+min(i+dfs(ones[i]-n1, i-1), dfs(n1, i-1))
    }

}






