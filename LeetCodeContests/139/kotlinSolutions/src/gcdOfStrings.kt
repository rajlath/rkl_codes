class Solution
{
    fun gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)

    fun gcdOfStrings(str1:String, str2:String):String
    {
        var lens = gcd(str1.length, str2.length)
        var str3 = str1.substring(0, lens)
        if((isMatch(str1, str3)) and isMatch(str2, str3)) return str3
        return ""
    }


    fun isMatch(s1:String, s2:String):Boolean
    {
        for(i in s1.indices)
        {
            if (s1[i] != s2[i % s2.length]) return false
        }
        return true
    }


}

fun main(args:Array<String>)
{
    println(Solution().gcdOfStrings("ABCABC", str2 = "ABC"))
}