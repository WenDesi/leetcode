class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 1
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] < 1 or nums[i] > len_nums:
                nums[i] = 0

        for i in range(len_nums):

            j = i
            while nums[j] != 0:
                index = nums[j]
                if index == j + 1:
                    break
                if nums[index-1] == index:
                    break
                nums[j],nums[index-1] = nums[index-1],nums[j]

        for i in range(len_nums):
            if nums[i] !=i+1:
                return i+1

        return len_nums+1

if __name__ == '__main__':
    wds= Solution()
    print wds.firstMissingPositive([1,1])
