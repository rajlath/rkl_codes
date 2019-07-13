package com.rklath.AdventureGame

class Dice
{
    var rolledValue = (1..6).shuffled().first()

}

fun main()
{
    var dice = Dice()
    println(dice.rolledValue)
}