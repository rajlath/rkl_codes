import java.lang.StringBuilder

fun main(args:Array<String>)
{
    var current = "Raj"
    var answer1 = ""
    answer1 = answer1.plus(current).plus(" ").plus("lath")
    println(answer1)

    var answer2 = current + " " + "lath"
    println(answer2)

    var answer3 = "lath"
    var answer4 = "$current $answer3"
    println(answer4)

    var builder = StringBuilder()
    builder.append(current).append(" ").append(answer3)
    println(builder.toString())
}