fun main(args:Array<String>)
{
    var string1 = "rajlath"
    var string2 = "lathjar"
    println(usingSort(string1, string2))
    println(usingCount(string1, string2))
}

/*
    *Givern two string check is one is permutation of another
    * param string1 : String
    * parma String2 : String
    * return Boolean true if they are permuation else false
 */

//method : Sort both string , and check char by char
private fun usingSort(str1:String, str2:String):Boolean
{
    val sorted_string1 = String(str1.toCharArray().sortedArray())
    val sorted_string2 = String(str2.toCharArray().sortedArray())
    for ( i in sorted_string1.indices)
    {
        if (sorted_string1[i] != sorted_string2[i])
            return false
    }
    return true

}

//* method : match char count of both the string
private fun usingCount(str1:String, str2:String):Boolean
{
    var chars1 = getCharCount(str1)
    var chars2 = getCharCount(str2)
    for ( i in chars1.indices)
    {
        if (chars1[i] != chars2[i]) return false
    }
    return true

}

private fun getCharCount(str:String):IntArray
{
    var countArr = IntArray(128)
    for (i in str)
    {
        countArr[i.toInt()] ++
    }
    return countArr

}