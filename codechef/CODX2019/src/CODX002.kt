/*
fun main(args:Array<String>)
{
    var nbTest = read().map(String::toInt)[0]
    while(nbTest > 0)
    {
        solve()
        nbTest --

    }
}

private fun read(delimit: Char = ' ') = readLine()!!.trim().split(delimit)

fun solve()
{


        var (amount, offer, offer_qty, cost) = read().map(String::toInt)
        var answer = amount / cost
        answer += ((answer / offer) * offer_qty)
        print(answer)


}

 */
fun main(args: Array<String>) {
    println(KotlinVersion.CURRENT)
}