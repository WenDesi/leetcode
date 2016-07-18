# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addTree(self, preorder_start,preorder_end,inorder_start,inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        head_num = self.preorder[preorder_start]
        head = TreeNode(head_num)
        head_index = self.dict[head_num]

        length = head_index - inorder_start + 1

        head.left = self.addTree(preorder_start+1,preorder_start + length,inorder_start,head_index)
        head.right = self.addTree(preorder_start + length,preorder_end,head_index+1,inorder_end)

        return head


    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None

        self.preorder = preorder
        self.inorder = inorder
        self.dict = {}

        i = 0
        for ele in inorder:
            self.dict[ele] = i
            i += 1

        return self.addTree(0,len(preorder),0,len(inorder))

if __name__ == '__main__':
    wds= Solution()
    print wds.buildTree([1,2,3],[2,3,1])