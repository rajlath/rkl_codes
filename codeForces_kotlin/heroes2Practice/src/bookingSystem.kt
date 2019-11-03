import java.util.*
data class Requests(val id:Int, val size:Int, val spend:Int)
data class Tables(val id:Int, val size:Int, var occupied:Boolean = false)
data class Reserve(val request:Int, val table:Int, val cost:Int)

fun main()
{
    make_reserveration()
}

fun make_reserveration()  = with(Scanner(System.`in`))
{
    val n = nextInt()
    val requests = Array<Requests>(n, { i -> Requests(i + 1, nextInt(), nextInt()) })
    val k = nextInt()
    val tables = Array<Tables>(k, { i -> Tables(i + 1, nextInt()) })
    var reserved = make_reservation(requests, tables)
    val income = reserved.sumBy { it.cost}

    println("${reserved.size} $income")
    for (p in reserved)
        println("${p.request} ${p.table}")

}

fun make_reservation(requests: Array<Requests>, tables: Array<Tables>): MutableList<Reserve>
{
    requests.sortByDescending { it.spend }
    tables.sortBy{it.size}
    val results = mutableListOf<Reserve>()
    for(r in requests)
    {
        for (t in tables)
        {
            if( t.occupied) continue
            if(t.size   >= r.size)
            {
                t.occupied = true
                results.add(Reserve(r.id, t.id, r.spend))
                break
            }
        }
    }
    return results

}

