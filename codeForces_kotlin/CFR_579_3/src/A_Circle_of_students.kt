fun main()
{
    val q = readLine()!!.toInt()
    repeat(q)
    {
        val len = readLine()!!.toInt()
        val arr = readLine()!!.split(" ").map{it.toInt()}
        val start = arr.indexOf(1)
        var flag1 = true
        var flag2 = true
        for (i in 0 until len)
        {
            if(arr[(start + i) % len] != i + 1) flag1 = false
            if(arr[(len+start-i)%len] != i+1)   flag2 = false
        }
        if(flag1 || flag2)
        {
            println("YES")
        }
        else
        {
            println("NO")
        }

    }
}