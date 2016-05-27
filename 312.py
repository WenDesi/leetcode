class Solution(object):
    def h(self, nums, l, r, d):
        if (l,r) not in d:
            d[(l,r)] = 0
            for i in range(l, r+1):
                d[(l,r)] = max(d[(l,r)], self.h(nums, l, i-1, d) + self.h(nums, i+1, r, d) + nums[i]*nums[l-1]*nums[r+1])
                if l == 1 and r == 4:
                    print i,':',d[(l,r)]
        return d[(l,r)]

    def maxCoins(self, nums):
        return self.h([1]+nums+[1], 1, len(nums), {})

if __name__ == '__main__':
    wds= Solution()
    print wds.maxCoins([3,1,5,8])
