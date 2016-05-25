# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = 0
    def hh(self,root,val):
        if root == None:
            return

        val += str(root.val)

        if root.left == None and root.right == None:
            self.result += int(val)
            return

        self.hh(root.left,val)
        self.hh(root.right,val)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        self.hh(root,'')
        return self.result
        