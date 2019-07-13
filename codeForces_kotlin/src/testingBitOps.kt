fun main(args:Array<String>)
{
    var x:Int
    var (a, b, c) = listOf<Int>(10, 30, 20)
    x = if(a > b)
    {
        doSomething()
        a
    }
    else if (b > c)
    {
        println("second")
        b
    }
    else
    {
        println("In third")
        c
    }
    println(x)
}
fun doSomething()
{
    println("Testing IFs")
}