# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        one = head
        two = head
        count = 0

        while count < 2:
            if one == two:
                count += 1
                if count == 2:
                    break
            one = one.next
            try:
                two = two.next.next
            except:
                break
        if count < 2:
            return None

        while head != one:
            head = head.next
            one = one.next
        return head