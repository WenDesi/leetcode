class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class LList(object):
    def __init__(self, start,end):
        self.start = start
        self.end = end
        self.next = None

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = LList(0,0)
        self.dict = {}

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if self.head.next == None:
            self.head.next = LList(val,val)
            self.dict[val] = 1
            return

        if val in self.dict:
            return

        self.dict[val] = 1

        has_left = val-1 in self.dict
        has_right = val+1 in self.dict

        if has_left and has_right:
            last = self.head
            now = self.head.next

            while now.end != val-1:
                last,now = now,now.next
            now.end = now.next.end
            now.next = now.next.next

        elif not has_left and has_right:
            last = self.head
            now = self.head.next

            while now.start != val+1:
                last,now = now,now.next
            now.start = val

        elif has_left and not has_right:
            last = self.head
            now = self.head.next

            while now.end != val-1:
                last,now = now,now.next
            now.end = val
        else:
            last = self.head
            now = self.head.next
            while now != None and now.end < val:
                last,now = now,now.next
            xin = LList(val,val)
            last.next = xin
            xin.next = now

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        result = []
        last = self.head
        now = self.head.next
        while now != None:
            result.append(Interval(now.start,now.end))
            last,now = now,now.next
        return result

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        wds = SummaryRanges()
        for num in nums:
            wds.addNum(num)

        results = wds.getIntervals()
        mmax = 0
        for inter in results:
            length = inter.end - inter.start
            mmax = max(mmax,length)
        return mmax

