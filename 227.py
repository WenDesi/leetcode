import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.replace(' ','')
        ele_list = re.findall(r'\d+|\+|\-|\*|\/', s)

        for i in range(len(ele_list)):
            try:
                ii = int(ele_list[i])
                ele_list[i] = ii
            except:
                pass

        stack = []
        i = 0
        while i < len(ele_list):
            ele = ele_list[i]
            if ele == '+' or ele == '-':
                stack.append(ele)
            elif ele == '*':
                stack[-1] = stack[-1] * ele_list[i+1]
                i+=1
            elif ele == '/':
                stack[-1] = stack[-1] / ele_list[i+1]
                i+=1
            else:
                stack.append(ele)
            i += 1

        result = stack[0]
        i = 0
        while i < len(stack):
            ele = stack[i]
            if ele == '+':
                result += stack[i+1]
                i += 1
            elif ele == '-':
                result -= stack[i+1]
                i+=1
            i += 1
        return result

if __name__ == '__main__':
    wds = Solution()
    print wds.calculate("1*2")