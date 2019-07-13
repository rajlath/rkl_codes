import kotlin.*

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map{ it.toLong() } // list of longs

fun main(){
    val (n,m) = readInts()
    val a = readInts().toIntArray()
    for(i in 1 until a.size){
        a[i]+= a[i-1]
    }
    val q = readInt()
    repeat(q){
        val k = readInts().toMutableList()
        k.add(m+1)
        var j = -1
        var ed = 0
        for(i in 1 until k.size){
            var d = (k[i]-1)-ed
            var bst = j
            var bed = a.size
            while(bst+1<bed){
                val mid = (bst+bed)/2
                val dd = a[mid]-(if(j!=-1)a[j] else 0)
                if(dd<=d){
                    bst = mid
                }else{
                    bed = mid
                }
            }
            j = bst
            ed = k[i]
        }
        print(if(j==a.size-1) "YES\n" else "NO\n")
    }
}