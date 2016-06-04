class Solution(object):
    def calculfanzhuan(self,s1,s2):
        self.reverse = []
        length = len(s1)

        for i in range(length):
            tmp = []
            for j in range(length):
                flag = True
                for t in range(j+1-i):
                    if s1[i+t] == s2[j-t]:
                        continue
                    flag = False
                    break
                tmp.append(flag)
            self.reverse.append(tmp)
        return

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dp = []
        length = len(s1)
        for i in range(length):
            tmp = []
            for j in range(length):
                tmp_j = [False for i in range(length+1)]
                tmp.append(tmp_j)
            dp.append(tmp)

        for l in range(1,length+1):
            for i in range(length-l+1):
                for j in range(length-l+1):
                    # flag = True
                    # for t in range(l):
                    #     if s1[i+t] == s2[j+l-t-1]:
                    #         continue
                    #     flag = False
                    #     break
                    # if flag:
                    #     dp[i][j][l] = True
                    #     continue

                    left = i+1
