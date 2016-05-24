class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j, i_, j_ = 0, 0, 0, -1
        while i < len(s):
            if j < len(p) and p[j] in [s[i], '?']:
                i, j = i + 1, j + 1

            elif j < len(p) and p[j] == '*':
                i_, j_ = i, j
                j += 1

            elif j_ > -1:
                i, i_ = i_ + 1, i_ + 1
                j = j_ + 1
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)

if __name__ == '__main__':
    wds= Solution()
    print wds.isMatch('aabbcc',"a*b*c")
