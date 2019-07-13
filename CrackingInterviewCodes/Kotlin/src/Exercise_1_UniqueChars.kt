fun main(args:Array<String>)
{
    val str1 = "rajkumar"
    val str2 = "rajkumlth"
    println(hashset_method(str1)) // will return false
    println(hashset_method(str2)) // will return true
    println(bitVector_method(str1)) // will return false
    println(bitVector_method(str2)) // will return true

}
/*
    * checks if all chars in a string is uniqe.
    * @param str : String
    * @return boolean : true if all chars are unique else false
 */


//* method 1 using Hashset
private fun hashset_method(str:String):Boolean
{
    var chars = BooleanArray(128)
    for (i in str)
    {
        var vals :Int = i - 'a'
        if(chars[vals]) return false
        chars[vals] = true
    }
    return true
}

//* method 2 using bitVector
private fun bitVector_method(str:String):Boolean
{
    var checker = 0
    for(i in str)
    {

        var value : Int = i - 'a'
        if((checker) and (1 shl value) > 0) return false
        checker = (checker or (1 shl value))
    }
    return true

}

