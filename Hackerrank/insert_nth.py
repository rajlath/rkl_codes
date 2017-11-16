"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
class Node(object):     
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def InsertNth(head, data, position):
    new_node = Node()
    new_node.data = data
    new_node.next = None
    
    if head.data == None:
        head = new_node
        return head
    if position == 0:
        new_node.next = head
        head = new_node
    else:
        done = 0
        temp = head
        while done < (position - 1):
            temp = temp.next
            done += 1
        new_node.next = temp
        temp.next = new_node
    return head  

node = Node()
for i in range(int(input())):
    d, p = [int(x) for x in input().split()]
    
    print(InsertNth(node, d, p).data, end="")


        
            
        
        
        
  
        
  
  
  
  
  
  
  
  
  
  
