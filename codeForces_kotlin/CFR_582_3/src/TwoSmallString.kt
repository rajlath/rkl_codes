fun main()
{
    val word = "abc"
    val list = word.toCharArray().toMutableList()
    val permList = permute(list)

    var n = readLine()!!.toInt()
    var s = readLine()!!.trim()
    var t = readLine()!!.trim()

    var answer = mutableListOf<String>()
    for (i in 0..permList.size - 1)
    {
        var cur = permList[i]
        var curr = StringBuilder()
        for (j in 0..n)
        {
            curr.append(cur)
        }

        answer.add(curr.toString())
        curr = StringBuilder()
        for (k in 0..n)
        {
            curr.append(cur[0])
        }
        for (k in 0..n)
        {
            curr.append(cur[1])
        }
        for (k in 0..n)
        {
            curr.append(cur[2])
        }
        answer.add(curr.toString())
    }

    var valid = "NO"
    var ans = ""
    for(i in 0..answer.size)
    {
        var curr = answer[i]

        if (curr.contains(s) || curr.contains(t)) continue
        else
        {
            valid = "YES"
            ans = curr
            break
        }

    }
    println(valid)
    if(valid == "YES") println(ans)

}

fun <String> permute(list:List <String>):List<List<String>>{
    if(list.size==1) return listOf(list)
    val perms=mutableListOf<List <String>>()
    val sub=list[0]
    for(perm in permute(list.drop(1)))
        for (i in 0..perm.size){
            val newPerm=perm.toMutableList()
            newPerm.add(i,sub)
            perms.add(newPerm)
        }
    return perms
}