fun main()
{
    var (n, k) = readLine()!!.split(" ").map { it.toInt()}
    var values = readLine()!!.split(" ").map { it.toInt()}
    var ans = mutableListOf<Int>()
    values.forEach()
    {
        if(! ans.contains(it))
        {
            if (ans.size >= k)
            {
                ans.removeAt(ans.size - 1)
            }
            ans.add(0, it)
        }
    }
    println(ans.size)
    ans.forEach()
    {
        print("$it ")
    }
}