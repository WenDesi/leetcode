# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        dict = {}
        rrand = []
        tt = head
        count = 0
        while tt:
            if tt not in dict:
                dict[tt] = count
                count += 1
            tt = tt.next
        tt = head
        while tt:
            rr = tt.random
            if rr == None:
                rrand.append(-1)
            else:
                rrand.append(dict[rr])
            tt = tt.next

        hh = RandomListNode(-1)
        fhead = hh
        tt = head
        count = 0
        wds = {}
        while tt:
            new_r = RandomListNode(tt.label)
            fhead.next = new_r
            fhead = fhead.next
            wds[count] = fhead
            count += 1
            tt = tt.next

        fhead = hh.next
        for index in rrand:
            if index == -1:
                fhead = fhead.next
                continue
            fhead.random = wds[index]
            fhead = fhead.next
        return hh.next

