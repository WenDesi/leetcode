class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        for num in nums1:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        result = []
        for num in nums2:
            if num in dict and dict[num] > 0:
                dict[num] -= 1
                result.append(num)