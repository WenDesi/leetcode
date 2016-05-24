class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island = 1
        island_count = 0

        if len(grid) == 0:
            return 0

        dp = [0 for i in range(len(grid[0])+1)]
        tmp = '0'*len(grid[0])
        grid.insert(0,tmp)

        for i in range(len(grid)):
            grid[i] = '0' + ''.join(grid[i])

        for t in range(1,len(grid)):
            m_list = grid[t]
            tmp = [0]
            for i in range(1,len(m_list)):
                if m_list[i] == '0':
                    tmp.append(0)
                    continue

                if dp[i] == 0 and tmp[i-1] == 0:
                    tmp.append(island)
                    island += 1
                    island_count += 1
                elif dp[i] == 0:
                    tmp.append(tmp[i-1])
                elif tmp[i-1] == 0:
                    tmp.append(dp[i])
                else:
                    this_island = dp[i]
                    that_island = tmp[i-1]
                    tmp.append(this_island)
                    if this_island == that_island:

                        continue

                    island_count -= 1

                    for j in range(len(dp)):
                        if dp[j] == that_island:
                            dp[j] = this_island

                    for j in range(len(tmp)):
                        if tmp[j] == that_island:
                            tmp[j] = this_island
            dp = tmp
        return island_count

if __name__ == '__main__':
    tt = ["111","010","111"]
    wds = Solution()
    print wds.numIslands(tt)