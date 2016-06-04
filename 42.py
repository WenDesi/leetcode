class Solution(object):
    def shuiwei(self,llist):
        result = 0
        i = 0
        while i < len(llist)-1:
            if llist[i] <= llist[i+1]:
                i += 1
                continue
            else:
                now = llist[i]
                i += 1
                while now > llist[i]:
                    result += now - llist[i]
                    i += 1
        return result

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0

        mmax = max(height)
        left = 0
        for i in range(len(height)):
            if height[i] == mmax:
                left = i
                break
        right = 0
        for i in range(len(height)-1,-1,-1):
            if height[i] == mmax:
                right = i
                break

        left_list = []
        for i in range(left+1):
            left_list.append(height[i])

        right_list = []
        for i in range(len(height)-1,right-1,-1):
            right_list.append(height[i])

        result = self.shuiwei(left_list) + self.shuiwei(right_list)

        left += 1
        while left < right:
            result += mmax - height[left]
            left += 1
        return result

if __name__ == '__main__':
    wds = Solution()
    print wds.trap([2,0,2])

