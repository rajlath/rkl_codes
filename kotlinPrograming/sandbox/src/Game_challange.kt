fun main(args:Array<String>)
{
    val name = "Madrigal"
    var healthPoints  = 89
    val isBlessed = true
    val isImmortal = false
    val karma = (Math.pow(Math.random(), (110 - healthPoints)/ 100.0 * 20 )).toInt()

    //Aura
    //if(isBlessed && healthPoints > 50 || isImmortal)
    val auraColor = auraColor(isBlessed, healthPoints, isImmortal, karma)

    //val auraColor = if (auraVisible) "Green" else "None"
    //println(auraColor)
    /*
    if(auraVisible)
    {
        println("Green")
    }else{
        println("None")
    }

     */

    /*

    //if(healthPoints == 100){
    val healthStatus = if(healthPoints == 100) {
        " is in excellent condition!."
        //}else if(healthPoints >= 90)
    }else if(healthPoints in 90..99)
    {
        " has a few scratches."
        //println()
    }
    //else if(healthPoints >= 75)
    else if(healthPoints in 75..89)
    {
        if(isBlessed)
        {
            " has some minor wounds but is healing quite quickly!."
            //println(name +" has some minor wounds but is healing quite quickly!.")
        }else{
            " has some minor wounds."
            //println(name + " has some minor wounds.")
        }

    }
    //else if(healthPoints >= 15)
    else if (healthPoints in 15..74)
    {
        " looks pretty hurt."
        //println(name + " looks pretty hurt.")
    }else{
        " is in awful condition!."
        //println(name + " is in awful condition!.")
    }

     */


    /*
    val healthStatus = if(healthPoints == 100)" is in excellent condition!."
                       else if(healthPoints >= 90) " has a few scratches."
                       else if(healthPoints >= 75)
                            if(isBlessed) " has some minor wounds but is healing quite quickly!."
                            else " has some minor wounds."
                       else if(healthPoints >= 15) " looks pretty hurt."
                       else " is in awful condition!."

     */

    val healthStatus = formatHealthStatus(healthPoints, isBlessed)

    //aura
    println("(Aura Color :  $auraColor)" + "(Blessed: ${if(isBlessed) "Yes" else "No" })" )
    //println("(Aura Color : ${if(isBlessed) auraColor else "None )" +  " )
    //println("(Aura: $auraColor)" + "(Blessed : ${if(isBlessed) "Yes" else "No" })")

    //player status
    println("Name and status of the player :$name $healthStatus")
    castFireball(20)
    return
}

private fun auraColor(
    isBlessed: Boolean,
    healthPoints: Int,
    isImmortal: Boolean,
    karma: Int
): String {
    val auraVisible = isBlessed && healthPoints > 50 || isImmortal
    val auraColor = when (karma) {
        in 0..5 -> "red"
        in 6..10 -> "orange"
        in 11..15 -> "purple"
        else -> "green"

    }
    return auraColor
}

private fun formatHealthStatus(healthPoints: Int, isBlessed: Boolean) =
        when (healthPoints) {
        100 -> " is in excellent condition!."
        in 90..99 -> " has a few scratches."
        in 75..89 -> if (isBlessed) " has some minor wounds but is healing quite quickly!."
        else " has some minor wounds."
        in 15..74 -> " looks pretty hurt."
        else -> " is in awful condition!."


}

private fun castFireball(numFireball:Int = 5) =
    println("A glass of Fireball springs into exitstence.(x$numFireball)")
