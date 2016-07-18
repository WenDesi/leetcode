class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0


        left = [0]
        mmin = prices[0]
        for i in range(1,len(prices)):
            new = max(left[-1],prices[i]-mmin)
            left.append(new)
            mmin = min(mmin,prices[i])

        print left

        right = [0]
        reverse = prices[::-1]
        mmax = reverse[0]
        for i in range(1,len(reverse)):
            new = max(right[-1],mmax-reverse[i])
            right.append(new)
            mmax = max(mmax,reverse[i])
        right = right[::-1]
        print right

        result = 0
        for i in range(len(prices)-1):
            result = max(result,left[i]+right[i+1])
        return max(result,max(left))

if __name__ == '__main__':
    wds= Solution()
    print wds.maxProfit([1,2,4])