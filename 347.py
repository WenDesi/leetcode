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
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mtimes = {}
        results = []

        for num in nums:
            if num not in mtimes:
                mtimes[num] = 1
            else:
                mtimes[num] += 1

        heap = mHeap(False)
        for a1 in mtimes:
            heap.push([mtimes[a1],a1])

        for i in range(k):
            top = heap.top()
            results.append(top[1])
            heap.pop()
        return results

if __name__ == '__main__':
    wds = Solution()
    print wds.topKFrequent([1],1)