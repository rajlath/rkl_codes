class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end   = end
        self.total = 0
        self.left  = None
        self.right = None
        
class NumArray(object):
    def __init__(self, nums):
        def create_tree(nums, l, r):
            
            if l > r :
                return None
            
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
                
            mid = (l + r) // 2
            root = Node(l, r)
            
            root.left = create_tree(nums, l, mid)
            root.right= create_tree(nums, mid + 1, root.right)
            
            root.total = root.left.total + root.right.total
            return root
        self.root = create_tree(nums, 0, len(nums)-1) 
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        def update_value(root, i, val):
            
            if root.start == root.end:
                root.total = val
                return val
            
            mid = (root.start + root.end) // 2
            if i <= mid:
                update_value(root.left, i, mid)
            else:
                update_value(root.right, mid+1, root.right)
            root.total = root.left.total + root.right.total
            
            return root.total
            
        return updateVal(self.root, i, val)
        
            
    def sum_range(self, i, j): 
        
        def range_sum(root, i, j):
            
            if root.start == i and root.end == j:
                return root.total
                
            mid = (root.start + root.end) // 2
            
            if j <= mid:
                return range_sum(root.left, i, j)
            if j >= mid+1:
                return range_sum(root.right, i, j) 
                 
        return range_sum(self.root, i, j)  
        
                
                
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2) 
'''
3 4
1 3 0
2 -1 10
3 1 3
1 3 1
2 2 5
3 1 3
''' 
noe, noq = [int(x) for x in input().split()]
arra = [int(x) for x in input().split()]
narra = NumArray(arra)
arrb = [int(x) for x in input().split()]
narrb = NumArray(arrb)
for _ in range(noq):
    arr = [int(x) for x in input().split()]
    if arr[0] == 1:
        narra.update(arr[1], arr[2])
        print(narra)
    elif arr[0] == 2:
        narrb.update(arr[1], arr[2])
        print(narrb) 
           
    

                 
                
                       
                        
        
           
                
                
                    
    

