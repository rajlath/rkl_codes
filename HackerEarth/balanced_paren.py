'''
SAMPLE INPUT 
5
1 -1 2 3 -2
SAMPLE OUTPUT 
2
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
        
        
noe = int(input())
arr = [int(x) for x in input().split()]
stk = Stack()
last_max_run_index = 0
last_max_run_value = 0
ans = 0
for i in range(noe):
    if not stk.is_empty() and arr[i] < 0 and stk.peek() == (-1 * arr[i]):
        stk.pop()
        if last_max_run_index + 2 == i:
            max_run = last_max_run_value + 1
        else:
            max_run += 1        
        last_max_run_index = i
        last_max_run_value = max_run
        ans  = max(ans, max_run)
    else:
        stk.push(arr[i]) 
        max_run = 0
print(ans * 2)         
        
        

