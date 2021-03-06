class mHeap(object):
    heap = []

    def __init__(self,MIN_HEAP = True):
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
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = mHeap(False)
        for num in nums:
            heap.push([num])

        for i in range(k-1):
            heap.pop()

        top = heap.top()
        return top[0]
if __name__ == '__main__':
    wds = Solution()
    print wds.findKthLargest([2,1],2)