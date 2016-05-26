# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def gotoTree(self,root):
        if root.left == None and root.right == None:
            return (0,root.val)

        if root.left == None:
            left = (0,0)
        else:
            left = self.gotoTree(root.left)
        if root.right == None:
            right = (0,0)
        else:
            right = self.gotoTree(root.right)

        last = left[1]+right[1]
        now = max(last,left[0]+right[0]+root.val)
        result = (last,now)
        return result



    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        result = self.gotoTree(root)
        return max(result[0],result[1])