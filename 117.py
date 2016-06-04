# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return
        next_start = root
        while True:

            wds = []
            head = None
            start = None
            while len(wds) != 0 or next_start != None:
                if len(wds) == 0:
                    wds.append(next_start.left)
                    wds.append(next_start.right)
                    next_start = next_start.next

                if wds[0] == None:
                    wds.pop(0)
                    continue

                if head == None:
                    start = wds[0]
                    head = wds[0]
                    wds.pop(0)
                    continue

                head.next = wds[0]
                head = head.next
                wds.pop(0)
            if start == None:
                break
            next_start = start

if __name__ == '__main__':
    mmin = 100
    # for i in range(2000001):
    #     score = calcul(i)
    #     if score < mmin:
    #         mmin = score

   #         print i
    print calcul(1002000)




