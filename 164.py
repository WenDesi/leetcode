#encoding=utf-8
import math

def sort(a, radix=10):
    max_a = max(a)
    K = int(math.ceil(math.log(max_a, radix)))
    if radix ** K == max_a:K += 1
    bucket = [[] for i in range(radix)]
    for i in range(1, K+1):
        for val in a:
            bucket[val%(radix**i)/(radix**(i-1))].append(val)
        del a[:]
        for each in bucket:
            a.extend(each)
        bucket = [[] for i in range(radix)]

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        sort(nums)
        print nums
        maxx = 0
        for i in range(len(nums)-1):
            maxx = max(maxx,nums[i+1]-nums[i])
        return maxx

if __name__ == '__main__':
    wds= Solution()
    print wds.maximumGap([1,10])