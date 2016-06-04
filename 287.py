class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        circle_length = len(nums)

        for i in range(len(nums)):
            length = 0
            wds = i+1
            while wds != nums[i]:
                last = i
                i = nums[i] - 1

                # if i+1 == nums[i] and nums[i] == last:
                #     return i+1

                length += 1
                if length > circle_length:
                    onestep = wds - 1
                    twostep = wds - 1

                    onestep = nums[onestep] - 1
                    twostep = nums[onestep] - 1

                    while nums[onestep] != nums[twostep]:
                        onestep = nums[onestep] - 1
                        twostep = nums[twostep] - 1
                        twostep = nums[twostep] - 1

                    twostep = wds - 1
                    while twostep != onestep:
                        onestep = nums[onestep] - 1
                        twostep = nums[twostep] - 1
                    return onestep + 1
        return 0

if __name__ == '__main__':
    wds = Solution()
    print wds.findDuplicate([2,5,9,6,9,3,8,9,7,1])