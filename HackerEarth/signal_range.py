'''
1
7
100 80 60 70 60 75 85
SAMPLE OUTPUT 
1 1 1 2 1 4 6
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
        
       

for _ in range(int(input()))        :
    noe = int(input())
    arr = [int(x) for x in input().split()]
    ans = [0] * noe
    stk = Stack() 
    ans[0] = 1
    stk.push(0)
    for i in range(1,noe):
        while (not stk.is_empty()) and stk.peek() != None and arr[stk.peek()] <= arr[i]:
            stk.pop()
                
        if stk.is_empty():            
            ans[i] =  i+1
        else:
            ans[i] = i - stk.peek()
        stk.push(i)
    print(" ".join(map(str, ans)))          
            
            
    
        

    


