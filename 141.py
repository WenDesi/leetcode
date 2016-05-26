# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False

        one = head
        two = head
        count = 0

        while count < 2:
            if one == two:
                count += 1
            one = one.next
            try:
                two = two.next.next
            except:
                break
        if count < 2:
            return False
        return True