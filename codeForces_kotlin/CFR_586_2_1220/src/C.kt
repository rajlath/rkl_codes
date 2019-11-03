fun main()
{
    val ins = readLine()!!
    val lens= ins.length
    var last='z'
    repeat(lens)
    {k->
        val ch = ins[k]
        println( if (last < ch) "Ann" else "Mike" )
        last = minOf(ch, last)
    }

}