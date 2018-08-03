fun <T : Comparable<T>> List<T>.quickSort(): List<T> =
    if(size < 2) this
    else {
        val pivot = first()
        val (smaller, greater) = drop(1).partition { it <= pivot}
        smaller.quickSort() + pivot + greater.quickSort()
    }
// Usage
fun main(array:Array<String>)
{
   var lst:List<String> = listOf("raj", "last", "lath", "onceina").quickSort() // [1,2,5]
   print(lst)
}
