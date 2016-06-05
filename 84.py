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

if __name__ == '__main__':
    wds= Solution()
    print wds.largestRectangleArea([2,1,2])
