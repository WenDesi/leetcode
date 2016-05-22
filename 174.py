class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])

        dp = []
        for ele_list in dungeon:
            tmp_list = []
            for ele in ele_list:
                tmp_list.append(0)
            dp.append(tmp_list)

        last = 1
        for i in range(m-1,-1,-1):
            last = dp[i][n-1] = max(last - dungeon[i][n-1],1)

        last = 1
        for i in range(n-1,-1,-1):
            last = dp[m-1][i] = max(last - dungeon[m-1][i],1)

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = max(1,min(dp[i+1][j],dp[i][j+1])-dungeon[i][j])

        return dp[0][0]



if __name__ == '__main__':
    wds= Solution()
    print wds.exist(["ABCE","SFCS","ADEE"],"ABCCED")