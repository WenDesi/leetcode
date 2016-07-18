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
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = mHeap(False)

        for i in nums1:
            for j in nums2:
                if len(heap.heap) < k:
                    heap.push([i+j,[i,j]])
                else:
                    top = heap.top()
                    if i+j < top[0]:
                        heap.pop()
                        heap.push([i+j,[i,j]])

        result = []
        for ele in heap.heap:
            result.append(ele[1])
        return result

if __name__ == '__main__':
    wds = Solution()
    print wds.kSmallestPairs([1,1,2],[1,2,3],2)