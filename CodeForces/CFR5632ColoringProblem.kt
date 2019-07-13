//thanks to proizvedenie
fun main()
{
    var n = readLine()!!.toInt()
    var arr = IntArray(n + 1)
    var akk = 1
    for (i in 2..n)
    {
        if(arr[i] == 0)
        {
            for (j in i..n step i)
            {
                arr[j] = akk
            }
            akk ++
        }
    }
    println(arr.drop(2).joinToString(" "))
}