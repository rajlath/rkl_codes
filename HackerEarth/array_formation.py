from __future__ import print_function
'''
'''
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
        
        

def sundaram3(max_n=100000) :
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4
    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)
'''
5
7 21 18 3 12
'''            

           
prime_s = sundaram3()
stck = Stack()
que   = Queue()
nos = input()
arr = [int(x) for x in raw_input().split()]
for i in arr:
    if i in prime_s:
        que.enqueue(i)
    else:
        stck.push(i) 
while not que.isEmpty():
    print(que.dequeue(),end=" ")
print()    
while not stck.isEmpty():
    print(stck.pop(), end=" ")
print()
               

   

