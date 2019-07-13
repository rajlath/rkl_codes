fun main(args:Array<String>)
{
    solve()
}

private fun read(delimit: Char = ' ') = readLine()!!.split(delimit)

private fun solve()
{
    var nbTest = read().map(String::toInt)[0]
    while(nbTest > 0)
    {
        var lens = read().map(String::toInt)[0]
        var ins  = read()[0]
        var vowels = "aeiou"
        var ans = 0
        if (lens >= 2) {
            for (i in 0..ins.length - 2) {
                if (vowels.contains(ins[i])) continue
                else {
                    if (i != lens) {
                        if (vowels.contains(ins[i + 1])) {
                            ans++
                        }

                    }

                }

            }
        }
        println(ans)



        nbTest --
    }
}