# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    dp = [TreeNode(1)]
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        for i in range(1,n+1):
            num = i
            tmp = []
            for sm_tree in self.dp:
                tree = TreeNode(num)
                root = sm_tree
                while root != None:
                    tmp.append()
