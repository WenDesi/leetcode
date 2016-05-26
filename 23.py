# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class mHeap(object):
    heap = []

    def __init__(self,MIN_HEAP = True):
        self.heap = []
        self.MIN_HEAP = MIN_HEAP

    def cal(self,i,j):
        if self.MIN_HEAP:
            return i[0] < j[0]
        return i[0] > j[0]

    def cal_equal(self,i,j):
        if self.MIN_HEAP:
            return i[0] <= j[0]
        return i[0] >= j[0]

    def top(self):
        return self.heap[0]

    def push(self,element):
        i = len(self.heap)
        self.heap.append(element)

        j = (i-1)/2
        tmp = element
        while( j >= 0 and i != 0 ):
            if self.cal(self.heap[j],tmp):
                break
            self.heap[i] = self.heap[j]
            i =j
            j = ( i - 1 ) / 2
        self.heap[i] = tmp

    def pop(self):
        if len(self.heap) == 0:
            return

        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) == 0:
            return
        self.fix_down()

    def fix_down(self):
        i = 0
        j = 2 * i + 1
        n = len(self.heap)

        tmp = self.heap[i]

        while j < n:
            if j + 1 < n and self.cal(self.heap[j+1],self.heap[j]):
                j += 1
            if self.cal_equal(tmp,self.heap[j]):
                break

            self.heap[i] = self.heap[j]
            i = j
            j = 2 * i + 1

        self.heap[i] = tmp

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = mHeap()

        if len(lists) < 2:
            return lists

        for i in range(len(lists)):
            wds = lists[i]

            if wds == None:
                lists[i] = ListNode(21474836474)
            else:
                while wds.next != None:
                    wds = wds.next
                wds.next = ListNode(21474836474)

            heap.push([lists[i].val,i])
            lists[i] = lists[i].next

        head = ListNode(0)
        result = head
        top = heap.top()
        while top[0] != 21474836474:
            new_node = ListNode(top[0])
            head.next = new_node
            head = head.next

            heap.pop()
            heap.push([lists[top[1]].val,top[1]])
            lists[top[1]] = lists[top[1]].next
            top = heap.top()
        return result.next

if __name__ == '__main__':
    ssc = ListNode(1)
    xj = [None,ssc]

    wds= Solution()
    print wds.mergeKLists(xj)

