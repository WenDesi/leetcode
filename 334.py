#encoding=utf-8

class Solution(object):
    def binary_search(self,num):
        start = 0
        end = len(self.LIS) - 1

        if self.LIS[0] >= num:
            return 0

        while end-start>1:
            middle = (start+end)/2

            if self.LIS[middle] > num:
                end = middle
            elif self.LIS[middle] < num:
                start = middle
            else:
                return middle

        return end


    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False


        self.LIS = [nums[0]]

        for i in range(1,len(nums)):
            num = nums[i]

            if num > self.LIS[-1]:
                self.LIS.append(num)
            else:
                index = self.binary_search(num)

                self.LIS[index] = num

            if len(self.LIS) > 2:
                return True

        return False


if __name__ == '__main__':
    testset = [1,2,1,2,1,1]

    wds = Solution()
    print wds.increasingTriplet(testset)
