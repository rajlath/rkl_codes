/*
1.6 String Compression:
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z)
*/

/*
param str String: String which is to be compressed
return String if compressed string is larger then original return original
*/
// uses normal method having a pointer to count repeatation

fun main(args : Array<String>)
{
    println(StringCompression("aabcccaabbcc")) //compressed len is less so answer is compressed string
    println(StringCompression("aabccaabbcc")) // compressed len is more so answer is original string
}
private fun buildCompressed(comp:String, chrs:Char, cnt:Int):String
{
    var compressed = comp
    compressed += chrs
    compressed += cnt.toString()
    return compressed
}

private fun StringCompression(strs:String):String
{
    var compressed = ""
    var consecutiveCount = 0
    for ( i in strs.indices)
    {
        consecutiveCount ++
        var further = i + 1
        if (further >= strs.length)
        {
            compressed = buildCompressed(compressed, strs[i], consecutiveCount)
            consecutiveCount = 0
        }
        else if (strs[further] != strs[i])
        {
            compressed = buildCompressed(compressed, strs[i], consecutiveCount)
            consecutiveCount = 0

        }
    }
    if(compressed.length > strs.length) compressed = strs
    return compressed
}