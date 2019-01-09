# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        def isCompleteTree(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            if root is None: return True
            queue = []
            flag  = False
            queue.append(root)
            while(len(queue) > 0):
                tempNode = queue.pop(0)
                if (tempNode.left):
                    if flag == True : return False
                    queue.append(tempNode.left)
                else: flag = True
                if(tempNode.right):
                    if flag == True: return False
                    queue.append(tempNode.right)
                else:
                    flag = True
            return True
