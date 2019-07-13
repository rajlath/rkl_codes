import kotlin.math.absoluteValue

/*
One Away: There are three types of edits that can be performed on strings:
insert a character,remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
*/
/*
params src String
params tgt String
return boolean
return true if both the string can be made equal
1. by replacing a letter in either src or tgt
2. Adding a letter in either
3. removing a letter in either
*/

fun main(args:Array<String>)
{
    println(one_edit_away("rajlath", "rajloth")) // return True a at index 4 should be replaced
    println(one_edit_away("rajlath", "rajath"))  // 'l' to be added at index 3 return True
    println(one_edit_away("rajlth", "rajlath"))  // 'a' to be added at index 4 return True
    println(one_edit_away("rajlath", "rakloth")) // return False two mismatch
}

private fun  one_edit_away(src:String, tgt:String):Boolean
{
    var lens = src.length
    var lent = tgt.length
    if ((lens - lent).absoluteValue <= 1)
    {
        if (lens == lent) return one_edit_replacement(src, tgt)
        else return one_edit_insert(src, tgt)
    }
    else return false
}

private fun one_edit_replacement(src:String, tgt:String):Boolean
{
    var one_difference = false
    for(i in src.indices)
    {
        if (src[i] != tgt[i])
        {
            if (one_difference) return false
            else one_difference = true
        }
    }
    return true
}

private fun one_edit_insert(src:String, tgt:String):Boolean
{
    var srci = 0
    var tgti = 0
    var difference_done = false
    while ((srci < src.length) and (tgti < tgt.length))
    {
        if (src[srci] != tgt[tgti])
        {
            if(difference_done) return false
            else
            {
                if (src.length > tgt.length) srci ++
                else tgti++
                difference_done = true
            }
        }
        else
        {
            srci ++
            tgti ++

        }


    }
    return true
}

