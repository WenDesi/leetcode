class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        wds = {}
        result = []
        for i in range(len(s)-9):
            tmp = s[i:i+10]
            if tmp in wds:
                wds[tmp] += 1
                if wds[tmp] == 2:
                    result.append(tmp)
            else:
                wds[tmp] = 1
        return result

if __name__ == '__main__':
    wds = Solution()
    print wds.findRepeatedDnaSequences("AAAAAAAAAAA")