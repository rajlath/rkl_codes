fun main(args: Array<String>)
{
    val i:Int = 6
    if (i in 10..20 ){ println("We have your number.") } else { println("No we don't have it.")}

    val x:Int = 2
    when(x)
    {
        1, 2 -> print("Number is in range.\n")

        else ->
        {
            print("Number is above range.")
        }
    }

    var listOf : List<Int> = listOf(1, 2, 3, 4, 5)
    for (i in listOf){ println(i) }
}