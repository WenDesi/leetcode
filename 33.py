class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums)-1

        while end-start>1:
            pivot = (end+start)/2
            if nums[pivot] == target:
                return pivot
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

            if nums[start] < nums[end]:
                if nums[pivot] > target:
                    end = pivot
                else:
                    start = pivot
            else:
                if nums[pivot] < nums[end] and target < nums[pivot]:
                    end = pivot
                elif target >= nums[start] and target >= nums[end] and target < nums[pivot]:
                    end = pivot
                elif target > nums[start] and target > nums[end] and target > nums[pivot] and nums[pivot] < nums[start]:
                    end = pivot
                elif target < nums[pivot] and target >= nums[start]:
                    end = pivot
                else:
                    start = pivot
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1