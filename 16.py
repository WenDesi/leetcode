class Solution(object):
    def hehe(self,i):
        left = i+1
        right = len(self.nums)-1

        mmin = abs(self.nums[i] + self.nums[left] + self.nums[right] - self.target)
        wds = self.nums[i] + self.nums[left] + self.nums[right]
        while left != right:
            he = self.nums[i] + self.nums[left] + self.nums[right]
            ca = abs(he - self.target)
            if ca == 0:
                return he

            if mmin > ca:
                wds = he
                mmin = ca

            if he > self.target:
                right -= 1
                continue
            if he < self.target:
                left += 1
                continue
            return 0
        return wds






    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.target= target
        self.nums = sorted(nums)
        mmin = 2147483647
        wds = 214746323
        for i in range(len(nums)-2):
            hh = self.hehe(i)
            if hh == self.target:
                return target

            if abs(hh-self.target) < mmin:
                mmin = abs(hh-self.target)
                wds = hh
        return wds



if __name__ == '__main__':
    wds = Solution()
    print wds.threeSumClosest([0,1,2],3)
