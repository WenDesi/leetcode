class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """


        n = min(n,m*2)
        result = m
        for i in range(m+1,n):
            result &= i
        return result

if __name__ == '__main__':
    i = 1
    while i < 2147483648:
        print i
        i *= 2
