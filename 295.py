import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)
    def reform_maxheap(self):
        while len(self.max_heap) > len(self.min_heap) + 1:
            top_item = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -1*top_item)

    def reform_minheap(self):
        while len(self.min_heap) > len(self.max_heap):
            top_item = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1*top_item)

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        try:
            mmax = self.max_heap[0]
        except:
            mmax = 0

        if mmax <= num:
            heapq.heappush(self.max_heap, num)
            self.reform_maxheap()
        else:
            heapq.heappush(self.min_heap, 0-num)
            self.reform_minheap()

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """

        len_1 = len(self.max_heap)
        len_2 = len(self.min_heap)

        if (len_1 + len_2) % 2 == 0:
            return (float(-1*self.min_heap[0]) + float(self.max_heap[0]))/2
        else:
            return self.max_heap[0]

if __name__ == '__main__':
    wds= MedianFinder()
    wds.addNum(-1)
    wds.addNum(-2)
    wds.addNum(-3)
    print wds.findMedian()


    # print wds.isMatch('aabbcc',"a*b*c")
