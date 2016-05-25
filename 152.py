class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp_min = [nums[0]]
        dp_max = [nums[0]]

        for i in range(1,len(nums)):
            tmp_min = nums[i]
            tmp_max = nums[i]

            tmp_min = min(tmp_min,min(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i]))
            tmp_max = max(tmp_max,max(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i]))

            dp_min.append(tmp_min)
            dp_max.append(tmp_max)


        return max(dp_max)

if __name__ == '__main__':
    fs = [-4,-3,-2]
    wds = Solution()
    print wds.maxProduct(fs)