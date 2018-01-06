class Node:
	def __init__(self,data):
		self.data = data
		self.nexts = None
		self.previous = None
	
class double_link_list:
	def __init__(self):
		self.head = None
		self.tail = None		
		self.size = 0
		self.mins = 1e9
		self.maxs = -1e9
		
		
	def add(self,value):
		new_node = Node(value)
		if self.head == None:
			self.head = new_node			
			self.tail = new_node
		else:
			tmp = self.tail			
			tmp.nexts = new_node
			self.tail = new_node
			self.tail.previous = tmp		
			
			
	def get_node_by_index(self,indx):
		if self.head == None:
			return -1
		else:
			curr = self.head
			for i in range(indx+1):
				curr = curr.nexts
				if curr == self.tail:
					return -1
			return curr.data
			
	def search_data(self, data):
		i =  -1
		if self.head == None:
			return i
		else:			
			curr = self.head
			while curr.nexts != None:
				if curr.data == data:
					return i
				curr = curr.nexts
				i += 1
			i += 1				
		return i	
	
	def remove_node(self,rnode):
		if self.head == None:
			return None
		tmp = rnode.previous
		tmp.nexts = rnode.nexts
		
	def __str__(self):
		
		lst = ""
		curr=self.head
		if curr != None:
			while curr.nexts != None:
				lst += str(curr.data)+" "
				curr = curr.nexts
			lst += str(curr.data)+" "	
		return(lst)		
	
					
dll = double_link_list()

dll.add(5)
dll.add(10)
dll.add(15)

print(dll)
print(dll.search_data(10))

				
		
				
										
					
									
			
			
			
				
			
		
	
	
	
		
	
