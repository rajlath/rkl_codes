fun readInts(delimit: Char =' ') = readLine()!!.split(delimit).map(String::toInt)


fun main(args:Array<String>)
{
    var lens = readInts()[0]
    var arr = readInts().sorted()
    var arr1 = arr.toSet()
    if (arr1.size == 1) println(-1)
    else println(arr.joinToString(separator = " "))

}