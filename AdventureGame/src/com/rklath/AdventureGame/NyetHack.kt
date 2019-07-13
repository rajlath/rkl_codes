package com.rklath.AdventureGame

fun main(args:Array<String>)
{
    val name = "Madrigal"
    var healthPoints = 84
    var isBlessed = true
    var isImmortal= false

    /* Aura */

    var auraVisible = auraColor(isBlessed, healthPoints, isImmortal)
    var healthStatus = formatHealthStatus(healthPoints, isBlessed)
    //player status
    printPlayerStatus(auraVisible, isBlessed, name, healthStatus)
    var inAbriation = castAFireSpell(10)
    println("Players inabriation level is : $inAbriation")
}

private fun printPlayerStatus(
    auraVisible: String,
    isBlessed: Boolean,
    name: String,
    healthStatus: String
) {
    println("(Aura : $auraVisible)" + "(Blessed : ${if (isBlessed) "YES" else "NO"})")
    println("$name $healthStatus")
}
/*
private fun com.rklath.AdventureGame.auraColor(isBlessed: Boolean, healthPoints: Int, isImmortal: Boolean): String {
    var auraVisible = if (isBlessed and (healthPoints > 50 || isImmortal)) "GREEN" else "NONE"
    return auraVisible
}
*/
private fun auraColor(isBlessed:Boolean, healthPoints: Int, isImmortal:Boolean) =
    if (isBlessed and (healthPoints > 50 || isImmortal)) "GREEN" else "NONE"


private fun formatHealthStatus(healthPoints: Int, isBlessed: Boolean) =
    when (healthPoints) {
        100 -> " is in excellent condition."
        in 90..99 -> " has a few scratches."
        in 75..89 -> if (isBlessed) {
            " has some minor wounds but is healing fast."
        } else {
            " has some minor wounds."
        }
        in 15..74 -> " looks pretty hurt."
        else -> " is in awful condition."
    }
    //return healthStatus


//private fun com.rklath.AdventureGame.castAFireSpell(numFireBalls:Int = 2) = println("A glass of Fireball springs into existence. (x$numFireBalls)")
/*
Inebriation level	Inebriation status
1-10	tipsy
11-20	sloshed
21-30	soused
31-40	stewed
41-50	..t0aSt3d

 */

private fun castAFireSpell(numFireBalls:Int = 2) =
        when(numFireBalls)
        {
            in 1..10 -> "tipsy"
            in 11..20 -> "sloshed"
            in 21..30 -> "soused"
            in 31..40 -> "stewed"
            else -> "..t0ast3d"
        }
