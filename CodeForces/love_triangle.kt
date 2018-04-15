fun main(args:Array<String>)
{
    var noe : Int  = readLine()!!.toInt()
    var arr : List<Int> = readLine()!!.trim().split(" ").map(String::toInt)
    var idx : Int  = 1
    var got        = false

    while (idx <= noe)
    {
        if (idx == arr[arr[arr[idx -1]-1]-1])
        {
            got = true
            break
        }
        idx += 1
    }
    if(got)
    {
        print("YES")
    }
    else
    {
        print("NO")
    }
}