import java.util.HashMap

fun main(args:Array<String>)
{
    var str = "atco cta  ssssssss"
    print(palin_permutation(str))
}

private fun palin_permutation(strs:String):Boolean
{
    var counts = mutableMapOf<Char, Int>()
    for (i in strs)
    {
        if(i.isWhitespace()) continue
        if (i in counts.keys) counts[i] = counts[i]!!.xor(1)
        else     counts[i] = 1
    }
    //println(counts)
    if (counts.values.sum() > 1)
    {
        return false
    }
    return true

}