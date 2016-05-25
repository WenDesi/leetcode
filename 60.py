class Solution(object):
    dp = [[1],[12,21]]
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        if n <= len(self.dp):
            return str(self.dp[n-1][k-1])

        for t in range(len(self.dp),n+1):
            tmp = []
            for num in self.dp[t-1]:
                num_str = str(num)
                for i in range(len(num_str)):
                    string = num_str[:i]+str(t+1)+num_str[i:]
                    tmp.append(int(string))
                string = num_str + str(t+1)
                tmp.append(int(string))
            self.dp.append(sorted(tmp))
        return str(self.dp[n-1][k-1])

if __name__ == '__main__':
    wds= Solution()
    print wds.getPermutation(3,3)


