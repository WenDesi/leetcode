class Solution(object):
    def replace(self,index,point,now_point):
        if now_point < 0:
            return

        if index >= len(self.s_list):
            if point == 0 and now_point == 0:
                ee = ''.join(self.s_list)
                self.result[ee] = 1
            return

        if self.s_list[index] == '(':
            self.replace(index+1,point,now_point+1)

            self.s_list[index] = ''
            self.replace(index+1,point-1,now_point)
            self.s_list[index] = '('

        elif self.s_list[index] == ')':
            self.replace(index+1,point,now_point-1)

            self.s_list[index] = ''
            self.replace(index+1,point-1,now_point)
            self.s_list[index] = ')'

        else:
            self.replace(index+1,point,now_point)

    def find_min_remove(self):
        self.wds = []
        self.ssc = []

        count = 0
        replace_count = 0
        for kuohao in self.s_list:
            if kuohao != '(' and kuohao != ')':
                continue
            if kuohao == '(':
                count += 1
                continue
            count -= 1
            if count < 0:
                replace_count += 1
                count = 0
                string = ''
        return count + replace_count

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        self.s_list = list(s)
        rep_count = self.find_min_remove()

        self.result = {}

        self.replace(0,rep_count,0)
        return list(self.result)






if __name__ == '__main__':
    wds= Solution()
    print wds.removeInvalidParentheses(")()))())))")