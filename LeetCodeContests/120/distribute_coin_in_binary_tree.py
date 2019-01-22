# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cnts={}
        sums={}
        def stat(root):
            if not root:
                return [0,0]
            l,r=stat(root.left),stat(root.right)
            cnt=1+l[0]+r[0]
            val=root.val+l[1]+r[1]
            cnts[root]=cnt
            sums[root]=val
            return [cnt,val]
        
        stat(root)
        
        def helper(root):
            if not root.left and not root.right:
                return 0
            if not root.left:
                delta=root.val-1
                root.right.val+=delta
                return abs(delta)+helper(root.right)
            if not root.right:
                delta=root.val-1
                root.left.val+=delta
                return abs(delta)+helper(root.left)
            cl,vl=cnts[root.left],sums[root.left]
            cr,vr=cnts[root.right],sums[root.right]
            dl=cl-vl
            dr=cr-vr
            root.left.val+=dl
            root.right.val+=dr
            return abs(dl)+abs(dr)+helper(root.left)+helper(root.right)
        return helper(root)
            
