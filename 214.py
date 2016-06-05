class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or s == s[::-1]:
            return s
        reverse = s[::-1]
        l = s +'#'+ reverse
        next = [0]*len(l)
        k = 0
        for i in range(1,len(l)):
            while k > 0 and l[k] != l[i]:
                k = next[k - 1]
            if l[k] == l[i]:
                k = k + 1
            next[i] = k
        print next
        # return s[next[-1]:][::-1] + s
        return reverse[: len(s) - next[-1]] + s

    def wds(self,s):
        rev_s = s[::-1]
        l = s + '#' + rev_s
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        print p
        return rev_s[: len(s) - p[-1]] + s

if __name__ == '__main__':
    wds= Solution()
    print wds.shortestPalindrome("abb")
    print wds.wds('abb')



