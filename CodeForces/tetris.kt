fun main(arg: Array<String>){
	val (n, m) = readLine().toString().split(" ").map{it.toInt()}
	val squares = readLine().toString().split(" ").map{it.toInt()}
	val finish = Array(n){ 0 }
	squares.forEach(){
		finish[it-1]++
	}
	println(finish.min())
}