class Solution(object):
    def ascend(self,i):
        if i+1 >= self.n:
            return

        pp = 1
        while i+1 < self.n and self.wds[i] < self.wds[i+1]:
            self.point[i] = pp
            i += 1
            pp += 1

        if i < self.n:
            self.point[i] = pp

        return i

    def descend(self,i):
        i = self.equal(i)
        if i >= self.n:
            return i

        j = i
        while i+1 < self.n and self.wds[i] > self.wds[i+1]:
            i += 1

        t = i
        pp = 1
        while t > j:
            self.point[t] = pp
            t -= 1
            pp += 1
        self.point[t] = max(self.point[t],pp)

        return i

    def equal(self,i):
        tt = self.wds[i]
        count = 0

        while i<self.n and self.wds[i] == tt:
            i += 1
            count += 1

        if i == self.n:
            self.equal_point += count - 1
            return i
        if count > 2:
            self.equal_point += count - 2
            return i-1
        return i-1

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        self.n = len(ratings)
        self.wds = ratings
        self.point = [0 for i in range(self.n)]
        self.point[0] = 1
        self.equal_point = 0

        i = 0
        shangshen = True
        while i+1 < self.n:
            if shangshen:
                i = self.ascend(i)
                shangshen = False
            else:
                i = self.descend(i)
                shangshen = True

        return sum(self.point) + self.equal_point


if __name__ == '__main__':
    wds= Solution()
    print wds.candy([1,2,2])