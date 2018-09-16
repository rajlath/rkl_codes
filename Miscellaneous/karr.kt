import java.util.Arrays;

fun main(args : Array<String>){
    val companies = arrayListOf<String>("Google", "Microsoft",
  "Facebook", "Apple", "JetBrains")
  companies.add("Amazon")
  for (comps in companies){ println(comps)}
}


