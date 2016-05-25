# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        wds = {}
        hashset = {}
        pointset = {}
        pointlist = []

        for point in points:
            if (point.x,point.y) not in pointset:
                pointset[(point.x,point.y)] = 1
                pointlist.append(point)
            else:
                pointset[(point.x,point.y)] += 1
        try:
            result = max(0,min(pointset[(points[0].x,points[0].y)],len(points)))
        except:
            return 0

        for i in range(len(pointlist)-1):
            for j in range(i+1,len(pointlist)):
                try:
                    a = float(pointlist[i].y - pointlist[j].y) / float(pointlist[i].x - pointlist[j].x)
                    b = -1.0
                    c = float(pointlist[i].y) - a * float(pointlist[i].x)
                except:
                    a = 0.0
                    b = 0.0
                    c = float(pointlist[i].x)

                ss = (a,b,c)
                if (a,b,c,j) in hashset:
                    continue

                if ss in wds:
                    wds[ss] += pointset[(pointlist[j].x,pointlist[j].y)]
                    hashset[(a,b,c,j)] = 1
                else:
                    wds[ss] = pointset[(pointlist[j].x,pointlist[j].y)] + pointset[(pointlist[i].x,pointlist[i].y)]
                    hashset[(a,b,c,i)] = 1
                    hashset[(a,b,c,j)] = 1


                if wds[ss] > result:
                    result = wds[ss]
        return result

if __name__ == '__main__':

    wds = Solution()
    p1 = Point(1,1)
    p2 = Point(1,1)
    p3 = Point(2,3)
    tt = [p1,p2]
    print wds.maxPoints(tt)
