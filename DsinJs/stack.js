class Stack
{
    constructor()
    {
        this.items = [];
    }

    push(element)
    {
        this.items.push(element);
    }
    pop()
    {
        return this.items.pop();
    }
    peek()
    {
        return this.items[this.items.length - 1];
    }
    isEmpty()
    {
        return this.items.length == 0;
    }
    size()
    {
        return this.items.length;
    }
    clear()
    {
        this.items = [];
    }
}

const stack = new Stack();
stack.push(12);
stack.push(15);
console.log(stack);
console.log(stack.peek()); // 15
stack.push(20);
console.log(stack.size());
console.log(stack.isEmpty());
stack.pop();
stack.pop();
console.log(stack.size()); //1
console.log(stack.peek()); // 12

