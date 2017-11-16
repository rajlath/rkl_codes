'''
SAMPLE INPUT 
5
5 4 1 3 2
SAMPLE OUTPUT 
-2 0 6 1 3 
'''

class Stack :
    '''Python implementation the stack'''
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
        
    def push(self,item):
        self.items.append(item)     
        
    def pop(self):
        try:
            return self.items.pop()
        except:
            return None    
        
    def peek(self):
        try:
            return self.items[len(self.items)-1]
        except:
            return None 
    
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return ' '.join([str(i) for i in self.items])    
        
import sys
noe = int(input())
arr = [int(x) for x in input().split()]
tmp = [0] * noe
stk = Stack()
stk.push(0)
i = 1


while i < noe:
    if arr[i] > arr[stk.peek()]:
        while not stk.is_empty():
            if arr[stk.peek()] < arr[i]:
                tmp[stk.peek()] = (i+1)
                stk.pop()
            else:
                break
    stk.push(i) 
    i += 1         
    
while not stk.is_empty():
    tmp[stk.peek()] = -1
    stk.pop()
    
while not stk.is_empty():stk.pop()
stk.push(noe - 1)
i = noe - 2
    
while i >= 0:    
    if arr[i] > arr[stk.peek()]:
        while not stk.is_empty():
            if arr[stk.peek()] < arr[i]:
                tmp[stk.peek()] += (i+1)
                stk.pop()
            else:
                break
    stk.push(i) 
    i -= 1
        
while not stk.is_empty():
    tmp[stk.peek()] += -1
    stk.pop()
    
    

        
print(" ".join(map(str, tmp)))        
    
                   
                    
    




                     
        

