fun main()
{
    val nb_test = readLine()!!.toInt()
    repeat(nb_test)
    {
        var (n, m) = readLine()!!.split(" ").map{it.toLong()}
        var tens = LongArray(11, { 0 } )
        for (i in 1..10)
        {
            tens[i] = (i * m) % 10
        }


        val div = (n / m) / 10
        val mod = (n / m) % 10 .toInt()
        var answer = div * tens.sum()
        answer += tens.slice(1..mod.toInt()).sum()
        println(answer)

    }
}
/*
nb_test = RI()
for _ in range(nb_test):
    n, m = RMI()
    tens = [(i * m) % 10 for i in range(1, 10) ]
    main, rest = divmod(n //m, 10)
    answ = main * sum(tens) + sum(tens[:rest])
    print(answ)
 */