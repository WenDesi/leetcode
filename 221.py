class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        stack = [-1]
        for height in heights:
            if height >= stack[-1]:
                stack.append(height)
            else:
                ll = []
                i = 1
                while height < stack[-1]:
                    ll.append(height)
                    result = max(result,i*stack[-1])
                    stack.pop()
                    i += 1
                stack.extend(ll)
                stack.append(height)

        for i in range(len(stack)):
            result = max(result,stack[i]*(len(stack)-i))
        return result

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        heights = [[0]*len(matrix[0])]
        for i in range(len(matrix)):
            tmp = []
            for j in range(len(matrix[0])):
                val = int(matrix[i][j])
                if val == 0:
                    tmp.append(0)
                else:
                    tmp.append(1+heights[-1][j])
            heights.append(tmp)
        heights = heights[1:]

        mmax = 0
        for height in heights:
            tmp_max = self.largestRectangleArea(height)
            mmax = max(mmax,tmp_max)
        return mmax

if __name__ == '__main__':
    wds= Solution()
    print wds.shortestPalindrome("abb")

