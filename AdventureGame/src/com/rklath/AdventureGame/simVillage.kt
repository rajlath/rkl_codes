package com.rklath.AdventureGame

fun main(args:Array<String>)
{
    val greetingFunction  =
    {
        playerName:String, numBuilding:Int ->
        val currentYear = 2019

        "Welcome to Sim Village ! $playerName (Copyright $currentYear) \n"+
        "You have to add $numBuilding houses "
    }
    runSimulation("Raj Lath", greetingFunction)
}

fun runSimulation(playerName:String,greetingFunction : (String, Int)->String )
{
    var numBuildings = (1..10).shuffled().last()
    println(greetingFunction(playerName, numBuildings))
}