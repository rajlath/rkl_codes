import java.util.*
data class IndVal(val indx:Int, val value:Int)

fun main()
{
    solve()
}

fun solve()  = with(Scanner(System.`in`))
{
    val n = nextInt()
    val indval = Array<IndVal>(n, { i -> IndVal(i + 1, nextInt())})
    do_solve(indval)

}

fun do_solve(indval: Array<IndVal>)
{
    indval.sortBy {it.value}
    print(indval)
    for (ist in indval)
    {
        print(ist)
    }
    var isOk = false
    for (i in 1..indval.size - 2)
    {
        if (indval[i-1].value < indval[i].value && indval[i].value < indval[i+1].value)
        {
            print("${indval[i-1].indx} ")
            isOk=true
        }

    }
    if(isOk==false)
    {
        println("-1 -1 -1")

    }




}