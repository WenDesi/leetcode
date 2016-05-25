class Solution(object):
    def hh(self,s):
        s_len = self.s_len
        self.dp = []

        if s_len == 0:
            return

        tmp = [True for i in range(s_len)]
        self.dp.append(tmp)
        if s_len == 1:
            return

        tmp = []
        for i in range(s_len-1):
            tmp.append(s[i] == s[i+1])
        self.dp.append(tmp)
        if s_len == 2:
            return

        for len in range(2,s_len):
            tmp = []
            for i in range(s_len):
                if i+len>=s_len:
                    break
                tmp.append((s[i]==s[i+len]) and (self.dp[len-2][i+1]))
            self.dp.append(tmp)

    def zhuanzhi(self):
        ano = []
        for i in range(self.s_len):
            tmp = [False for i in range(self.s_len)]
            ano.append(tmp)

        for i in range(self.s_len):
            for j in range(len(self.dp[i])):
                ano[j][i] = self.dp[i][j]

        self.dp = ano

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.dict = {}
        self.s_len = len(s)
        self.hh(s)


        tt = [0]
        for i in range(1,self.s_len):
            min_cut = i
            if self.dp[i][0]:
                tt.append(0)
                continue
            for j in range(i):
                if self.dp[j][i-j]:
                    min_cut = min(min_cut,tt[i-j-1] + 1)
            tt.append(min_cut)
        return tt[-1]




if __name__ == '__main__':
    fs = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
    # fs = 'bb'
    wds = Solution()
    print wds.minCut(fs)