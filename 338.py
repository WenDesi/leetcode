class Solution(object):
    dp = [0,1,1]
    def pow2last(self):
        len_dp = len(self.dp)
        count = 1
        while count < len_dp:
            count <<= 1
        return count >> 1

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if 1+num < len(self.dp):
            return self.dp[:num+1]

        last = self.pow2last()
        now = last << 1

        i = len(self.dp)
        while i <= num:
            if i == now:
                self.dp.append(1)
                last = now
                now = last << 1
            else:
                self.dp.append(self.dp[i-last]+1)
            i += 1
        return self.dp[:num+1]

if __name__ == '__main__':
    wds = Solution()
    print wds.countBits(5)