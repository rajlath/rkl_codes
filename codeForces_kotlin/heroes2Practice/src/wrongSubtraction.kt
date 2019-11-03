fun main()
{
    var (value, nos) = readLine()!!.split(" ").map{it.toInt()}
    for(i in 0..nos-1)
    {
        var mod = value % 10

        if(mod == 0)
        {
            value /= 10

        }
        else
        {
            value -= 1
        }
    }
    println(value)
}