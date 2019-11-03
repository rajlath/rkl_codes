fun main()
{
    val lens = readLine()!!.toInt()
    val given = readLine()!!
    val zcnt  = given.count{ it == 'z'}
    val ncnt  = given.count{ it == 'n'}
    var ans  = ""
    
    repeat(ncnt)
    {
        ans += "1 "
    }
    repeat(zcnt)
    {
        ans += "0 "
    }
    println(ans)


}