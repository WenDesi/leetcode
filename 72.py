class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_list = list(word1)
        word2_list = list(word2)

        min_len = min(len(word1),len(word2))
        max_len = max(len(word1),len(word2))
        if min_len == 0:
            return max_len

        dp = []
        for i in range(len(word1_list)):
            tmp = []
            for j in range(len(word2_list)):
                tmp.append(0)
            dp.append(tmp)

        ss = 1
        for i in range(len(word2_list)):
            ss = min(ss,int(not (word1_list[0] == word2_list[i])))
            dp[0][i] = ss + i

        ss = 1
        for i in range(len(word1_list)):
            ss = min(ss,int(not (word2_list[0] == word1_list[i])))
            dp[i][0] = ss + i

        for i in range(1,len(word1_list)):
            for j in range(1,len(word2_list)):
                dp[i][j] = min(dp[i-1][j-1] + int(not (word2_list[j] == word1_list[i])),min(dp[i-1][j],dp[i][j-1])+1)

        return dp[-1][-1]

if __name__ == '__main__':
    word1 = "sea"
    word2 = "ate"

    wds= Solution()
    print wds.minDistance(word1,word2)