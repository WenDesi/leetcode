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
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []


        heap = mHeap(False)

        for i in range(k):
            heap.push([nums[i],i])

        top = heap.top()
        result = [top[0]]

        for i in range(k,len(nums)):
            heap.push([nums[i],i])
            top = heap.top()
            while top[1] <= i-k:
                heap.pop()
                top = heap.top()
            result.append(top[0])
        return result

if __name__ == '__main__':
    wds = Solution()
    print wds.maxSlidingWindow([-95,92,-85,59,-59,-14,88,-39,2,92,94,79,78,-58,37,48,63,-91,91,74,-28,39,90,-9,-72,-88,-72,93,38,14,-83,-2,21,4,-75,-65,3,63,100,59,-48,43,35,-49,48,-36,-64,-13,-7,-29,87,34,56,-39,-5,-27,-28,10,-57,100,-43,-98,19,-59,78,-28,-91,67,41,-64,76,5,-58,-89,83,26,-7,-82,-32,-76,86,52,-6,84,20,51,-86,26,46,35,-23,30,-51,54,19,30,27,80,45,22],10)
