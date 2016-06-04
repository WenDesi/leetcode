# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.wds = self.digui(root)
        self.index = 0

    def digui(self,root):
        if root == None:
            return []

        wds = []
        t1 = self.digui(root.left)
        wds.extend(t1)
        wds.append(root.val)
        t2 = self.digui(root.right)
        wds.extend(t2)

        return wds


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index != len(self.wds)


    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.wds[self.index-1]

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())