class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 3:
            return max(nums[1],max(nums[0],nums[2]))

        rob = [0,0,nums[0]]
        nrob = [0,0,0]

        for i in range(1,len(nums)):
            wds = max(rob[i+1],rob[i]+nums[i])
            rob.append(wds)

            wds = max(nrob[i+1],nrob[i]+nums[i])
            nrob.append(wds)

        # print rob
        # print nrob
        return max(rob[-2],nrob[-1])

if __name__ == '__main__':
    wds = Solution()
    print wds.rob([2,1,1,2])