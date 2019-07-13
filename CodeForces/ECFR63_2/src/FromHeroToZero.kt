fun main()
{
    var nbTest = readLine()!!.toInt()
    while(nbTest > 0)
    {
        var (begin, divs) = readLine()!!.split(" ").map {it.toLong()}
        var ans = 0L
        while (begin > 0)
        {
            var mods = begin % divs
            begin = begin / divs
            ans += mods
            if (begin > 0) ans ++

        }
        println(ans)
        nbTest -= 1
    }
}

