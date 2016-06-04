# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):


    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key=lambda x: (x.start, -x.end))

        if len(intervals) < 2:
            return intervals

        start = intervals[0].start
        end = intervals[0].end
        result = []
        for i in range(1,len(intervals)):
            if end < intervals[i].start:
                result.append(Interval(start,end))
                start = intervals[i].start
                end = intervals[i].end
                continue
            end = max(end,intervals[i].end)
        result.append(Interval(start,end))
        return result

if __name__ == '__main__':
    wds = Solution()
    tt = [Interval(4,8),Interval(1,4),Interval(0,4)]
    wds.merge(tt)