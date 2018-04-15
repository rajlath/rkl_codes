import java.util.*

fun main(args:Array<String>)
{
    var ins = readLine()!!.split(' ').map(String::toInt).toIntArray()
    var y = ins[1]
    var x = ins[0]
    var ans  = "Yes"
    if (y  == 0) ans = "No"
    else if ((y ==1 ) && (x > 0)) ans = "No"
    else if (x < (y - 1)) ans = "No"
    else if (((x - y) % 2) == 0) ans = "No"
    println(ans)
}
