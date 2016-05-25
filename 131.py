class Solution(object):
    def huiwen(self,s):
        s_ = s[::-1]
        if s == s_:
            return True
        return False

    def backtrack(self,s,list_):
        if len(s) == 0:
            self.result.append(list_[:])
            return

        for i in range(1,len(s)+1):
            tmp_s = s[:i]
            next_s = s[i:]

            if self.huiwen(tmp_s):
                list_.append(tmp_s)
                self.backtrack(next_s,list_)
                list_.pop()



    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        self.backtrack(s,[])
        return self.result

if __name__ == '__main__':
    tt = 'aab'
    wds = Solution()
    print wds.partition(tt)