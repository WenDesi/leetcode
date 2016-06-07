class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        if len(s) == 0 or len(t) == 0:
            return 0

        dp = [0]
        for char in s:
            dp.append(dp[-1]+int(t[0]==char))
        dp[0] = 1

        for i in range(1,len(t)):
            this_row = [0]
            for j in range(len(s)):
                if i > j:
                    this_row.append(0)
                    continue
                this_row.append(this_row[-1])
                if t[i] == s[j]:
                    this_row[-1] += dp[j]
            dp = this_row
        return dp[-1]

if __name__ == '__main__':
    wds= Solution()
    print wds.numDistinct('ddd','dd')
