# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,root):
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return_val = max(left,right,0)

        self.mmax = max(self.mmax,left+right+root.val,return_val+root.val)
        return return_val + root.val

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mmax = -2147483648
        self.dfs(root)

        return self.mmax