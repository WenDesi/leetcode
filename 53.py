class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_max = [nums[0]]

        for i in range(1,len(nums)):
            tmp_max = nums[i]
            tmp_max = max(tmp_max,dp_max[i-1]+nums[i])
            dp_max.append(tmp_max)


        return max(dp_max)