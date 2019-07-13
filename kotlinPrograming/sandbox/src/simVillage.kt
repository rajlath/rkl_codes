fun main(args:Array<String>)
{
    val greetingFunction : () -> String = {
                val currentYear = 2019
                "Welcome to Sim Village Mayor ! (copyright $currentYear)"
    }
    println(greetingFunction())
}