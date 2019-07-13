fun main(args:Array<String>)
{
    var src = "rajkumarlath"
    var src1= "lathrajkumar"
    var src2 = "lathrajkumor"
    var src3 = "lathrajkuma"
    println(isStringRotation(src, src1))
    println(isStringRotation(src, src2))
    println(isStringRotation(src, src3))
}

private fun isStringRotation(src:String, tgt:String):Boolean
{
    if (src.length != tgt.length) return false
    var srcsrc = src + src
    return srcsrc.contains(tgt)
}