'''
class Solution {
public:
    vector<TreeNode*> splitBST(TreeNode* root, int V) {
        if (root == NULL) {
            return vector<TreeNode*>(2, NULL);
        } else if (root->val <= V) {
            auto lr = splitBST(root->right, V);
            root->right = lr[0];
            lr[0] = root;
            return lr;
        } else {
            auto lr = splitBST(root->left, V);
            root->left = lr[1];
            lr[1] = root;
            return lr;
        }
    }
};
'''

class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """

        if not root:
            return [None,None]
        if root.val==V:
            a=root.right
            root.right=None
            return [root,a]
        elif root.val<V:
            small,large=self.splitBST(root.right,V)
            root.right=small
            return [root,large]
        else:
            small,large=self.splitBST(root.left,V)
            root.left=large
            return [small,root]


sol = Solution()
print(sol.splitBST([4,2,6,1,3,5,7],2))





