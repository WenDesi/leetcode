import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        ele_list = [0]*len(s)

        for i in range(len(ele_list)):
            try:
                ii = int(s[i])
                ele_list[i] = ii
            except:
                ele_list[i] = s[i]

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

    def bfs(self,nums,llist):
        if len(nums) == 0:
            tmp_result = self.calculate(llist)
            if tmp_result == self.target:
                self.results.append(''.join(llist))
            return

        tmp_s = ''
        for i in range(len(nums)):
            tmp_s += nums[i]
            hh = nums[i+1:]
            llist.append('+')
            llist.append(tmp_s)
            self.bfs(hh,llist)
            llist[-2] = '-'
            self.bfs(hh,llist)
            llist[-2] = '*'
            self.bfs(hh,llist)
            llist.pop()
            llist.pop()


    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.target = target
        self.results = []

        if len(num) == 0:
            return []

        num_int = int(num)
        if num_int == target and str(target) == num:
            self.results.append(num)

        tmp = ''
        for i in range(len(num)-1):
            tmp += num[i]
            self.bfs(num[i+1:],[tmp])
        return self.results

if __name__ == '__main__':
    wds= Solution()
    print wds.addOperators('3456237490',9191)