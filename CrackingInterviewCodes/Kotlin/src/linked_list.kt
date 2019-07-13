class LinkedListNode<T>(value: T)
{
    var value:T = value
    var next :LinkedListNode<T>? = null
    var prev :LinkedListNode<T>? = null
}

class LinkedList<T>
{
    private var head:LinkedListNode<T>? = null
    var isEmpty:Boolean = head == null

    fun first():LinkedListNode<T>? = head

    fun last():LinkedListNode<T>?
    {
        var node = head
        if (node != null)
        {
            while(node?.next != null)
            {
                node = node?.next
            }
            return node
        }
        else
        {
            return null
        }
    }

    fun count():Int
    {
        var node = head
        if (node != null)
        {
            var counter = 1
            while(node?.next != null)
            {
                node = node.next
                counter += 1
            }
            return counter
        }
        return 0
    }

    fun nodeAtIndex(index:Int):LinkedListNode<T>?
    {
        if (index >= 0)
        {
            var node = head
            var i = index
            while(node != null)
            {
                if(i == 0) return node
                i -= 1
                node = node.next
            }

        }
        return null
    }

    fun append(value:T)
    {
        var newNode = LinkedListNode(value)
        var lastNode= this.last()
        if (lastNode != null)
        {
            newNode.prev = lastNode
            lastNode.next= newNode
        }
        else head = newNode
    }

    fun removeAll() { head = null}

    fun removeNode(node:LinkedListNode<T>):T
    {
        val prev = node.prev
        val next = node.next
        if (prev != null)
        {
            prev.next = next
        }
        else head = next
        next?.prev = prev
        node.prev  = prev
        node.next  = null
        return node.value
    }

    fun removeAtIndex(index:Int):T?
    {
        val node = nodeAtIndex(index)
        if(node != null)
        {
            return removeNode(node)
        }
        else
        {
            return null
        }

    }

    fun removeDups()
    {
        var done = mutableSetOf<String>()
        var node = head
        var previous = node?.prev
        while(node != null)
        {
            if (done.contains(node?.value.toString()))
            {
                previous?.next = node.next
            }
            else
            {
                done.add(node?.value.toString())
                previous = node
            }
            node = node?.next
        }
    }

    override fun toString():String
    {
        var s = "["
        var node = head
        while(node != null)
        {
            s += "${node.value}"
            node = node.next
            if(node != null) s += ","
        }
        return s +"]"
    }
}



fun main(args: Array<String>) {
    var ll = LinkedList<String>()
    ll.append("John")
    println(ll)
    ll.append("Carl")
    println(ll)
    ll.append("Zack")
    println(ll)
    ll.append("Tim")
    println(ll)
    ll.append("Tim")
    println(ll)
    ll.append("Steve")
    println(ll)
    ll.append("Peter")
    println(ll)
    ll.removeDups()
    println(ll)

    println("first item: ${ll.first()?.value}")
    println("last item: ${ll.last()?.value}")
    println("second item: ${ll.first()?.next?.value}")
    println("penultimate item: ${ll.last()?.prev?.value}")
    println("4th item: ${ll.nodeAtIndex(3)?.value}")
    println("The list has ${ll.count()} items")


}