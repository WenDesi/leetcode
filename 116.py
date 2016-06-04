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