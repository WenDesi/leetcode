# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k == 1 or head == None:
            return head

        length = 0
        tt = head
        while tt:
            length += 1
            tt = tt.next
        repeat_time = length / k

        before_head = ListNode(-1)
        before_head.next = head
        last_head = before_head
        thead = head
        for i in range(repeat_time):
            first = thead
            second = thead.next
            third = thead.next.next
            thead = second
            thead.next = first
            thead.next.next = third

            start = thead
            end = thead.next
            for i in range(k-2):
                tmp = end.next.next
                end.next.next = start
                start = end.next
                end.next = tmp
            last_head.next = start
            last_head = end
            thead = end.next
        return before_head.next

if __name__ == '__main__':
    wds = Solution()

    head = ListNode(1)
    t = head
    t.next = ListNode(2)
    t = t.next
    t.next = ListNode(3)
    t = t.next
    t.next = ListNode(4)
    t = t.next
    t.next = ListNode(5)
    t = t.next
    print wds.reverseKGroup(head,3)

