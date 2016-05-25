class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict = {}
        nums = sorted(nums)

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum in dict:
                    dict[sum].append([i,j])
                else:
                    dict[sum] = [[i,j]]

        result = {}
        for i in range(len(nums)):
            sum = 0 - nums[i]

            if sum not in dict:
                continue

            for tw in dict[sum]:
                if i in tw or i > tw[0]:
                    continue

                tt = (nums[i],nums[tw[0]],nums[tw[1]])
                result[tt] = 1

        return list(result)

if __name__ == '__main__':
    fs = [-1,0,1,2,-1,-4]
    wds = Solution()
    print wds.threeSum(fs)