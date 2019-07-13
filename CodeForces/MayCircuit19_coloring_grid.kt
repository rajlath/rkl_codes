import javax.swing.JPopupMenu

/*

fun readLongs(delimit: Char =' ') = readLine()!!.split(delimit).map(String::toLong)

fun com.rklath.AdventureGame.main(args:Array<String>)
{
    var (n, k) = readLongs()
    var ans = if (n == 2L) k * k  else k
    println(ans)

}

*/

fun main(args:Array<String>)
{
    var n = readLine()!!.toInt()
    var arr = readLine()!!.split(" ").map{ it.toInt()}.sorted()
    if(arr.take(n).sum() == arr.takeLast(n).sum()) println("-1")
    else println(arr.joinToString(" "))

}
