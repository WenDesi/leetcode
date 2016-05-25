class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        dict = {}
        nums = sorted(nums)
        print len(nums)

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum in dict:
                    dict[sum].append([i,j])
                else:
                    dict[sum] = [[i,j]]

        result = {}
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum = target - nums[i] - nums[j]

                if sum not in dict:
                    continue

                for tw in dict[sum]:
                    if i in tw or j in tw or j > tw[0] or j > tw[1]:
                        continue

                    tt = (nums[i],nums[j],nums[tw[0]],nums[tw[1]])
                    result[tt] = 1

        return list(result)

if __name__ == '__main__':
    fs = [2,1,0,-1]
    wds = Solution()
    print wds.fourSum(fs,2)