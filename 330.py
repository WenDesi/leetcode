class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """

        index_nums = 0
        hole = 1

        patche_count = 0
        nums.append(2147483647)

        while hole <= n:
            num = nums[index_nums]

            if hole >= num:
                hole += num
                index_nums += 1
            else:
                patche_count += 1
                nums.insert(index_nums,hole)

        return patche_count

if __name__ == '__main__':
    wds= Solution()
    print wds.minPatches([1,2,2],5)