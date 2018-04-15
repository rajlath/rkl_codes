/*
input
5
1 2 3 4 1
1 3
output
4
*/
fun main(args:Array<String>){
    val n=readLine()!!.toInt()
    val arr= readLine()!!.split(' ').map { it.toInt() }.toList()
    val (s,f) = readLine()!!.split(' ').map { it.toInt()-1 }

    var sum=arr.subList(s,f).sum()
    val ans=arr.withIndex().map { sum=sum-arr[(s+it.index)%n]+arr[(f+it.index)%n];sum }

    println(ans.reversed().withIndex().maxBy { it.value }!!.index+1)
}