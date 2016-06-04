# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key = lambda interval:interval.start)

        start = 0
        for interval in intervals:
            if newInterval.start > interval.end:
                start += 1
                continue
            break

        end = len(intervals) - 1
        while end >= 0:
            if newInterval.end < intervals[end].start:
                end -= 1
                continue
            break
        if end < 0:
            intervals.insert(0,newInterval)
            # for r in intervals:
            #     print r.start,':',r.end
            return intervals

        i = 0
        result = []
        while i != start:
            result.append(intervals[i])
            i += 1

        if start == len(intervals):
            intervals.append(newInterval)
            return intervals
        wds = Interval(min(newInterval.start,intervals[start].start),max(newInterval.end,intervals[end].end))
        result.append(wds)

        i = end + 1
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        for r in result:
            print r.start,':',r.end
        return result

if __name__ == '__main__':
    wds = Solution()
    t1 = Interval(1,5)
    # t2 = Interval(6,9)
    # t3 = Interval(6,7)
    # t4 = Interval(8,10)
    # t5 = Interval(12,16)

    tn = Interval(0,0)

    ll = [t1]
    wds.insert(ll,tn)
