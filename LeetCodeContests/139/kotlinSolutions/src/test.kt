fun main(args:Array<String>)
{
    println(1 in 1..3)
    println((1..3).toList())
    println(1 in 3 downTo 1)
    1 in 1 until 3
    3 in 1 until 3
    2 in 1..3
    2 !in 1..3
    println('x' in 'a'..'z')
}