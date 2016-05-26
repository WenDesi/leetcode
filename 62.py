class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mu = m + n - 2
        zi = min(m,n) - 1

        shangyihang = [1,1]
        if zi==0:
            return 1
        for i in range(2,mu):
            zheyihang = [1]
            for j in range(1,i):
                tmp = shangyihang[j-1] + shangyihang[j]
                zheyihang.append(tmp)
            zheyihang.append(1)
            shangyihang = zheyihang

        return shangyihang[zi-1] + shangyihang[zi]