fun main(args:Array<String>)
{
    val name = "Madrigal"
    var healthPoints  = 89
    val isBlessed = true
    val isImmortal = false

    //Aura
    //if(isBlessed && healthPoints > 50 || isImmortal)
    val auraVisible = isBlessed && healthPoints > 50 || isImmortal
    val auraColor = if (auraVisible) "Green" else "None"
    println(auraColor)
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

    val healthStatus = when(healthPoints)
    {
        100       -> " is in excellent condition!."
        in 90..99 -> " has a few scratches."
        in 75..89 -> if(isBlessed) " has some minor wounds but is healing quite quickly!."
                     else " has some minor wounds."
        in 15..74 -> " looks pretty hurt."
        else      -> " is in awful condition!."
    }

    //aura
    println("(Aura $auraColor)" + "(Blessed : ${if(isBlessed) "Yes" else "No" })")


    //player status
    println("Name and status of the player :$name $healthStatus")
}