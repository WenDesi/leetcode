import re
class Solution(object):
    def char_(self,s):
        if re.match('[0-9]',s):
            return 0
        if s == ' ':
            return 1
        if s == '.':
            return 2
        if s == 'e':
            return 3
        if s == '-' or s == '+':
            return 4
        return 5

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mechine = {0:{0:1,1:0,2:8,4:9},1:{0:1,1:7,2:2,3:4},2:{0:3,1:7,3:4},3:{0:3,1:7,3:4},4:{0:5,4:10},5:{0:5,1:7},6:{0:6,1:6,2:6,3:6,4:6,5:6},7:{1:7},8:{0:3},9:{0:1,2:8},10:{0:5}}
        end_mechine = [1,2,3,5,7]

        mechine_num = 0
        for ele in s:
            para = self.char_(ele)
            tmp_mechine = mechine[mechine_num]

            if mechine_num == 6:
                return False

            if para not in tmp_mechine:
                mechine_num = 6
            else:
                mechine_num = tmp_mechine[para]

        return mechine_num in end_mechine

if __name__ == '__main__':
    tt = "-1."
    wds= Solution()
    print wds.isNumber(tt)


