class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        s1_list = list(s1)
        s2_list = list(s2)
        s3_list = list(s3)

        last = [True]
        for i in range(len(s1_list)):
            last.append(last[-1] and s1_list[i] == s3_list[i])

        for i in range(len(s2_list)):
            now = [last[0] and s2_list[i] == s3_list[i]]
            for j in range(len(s1_list)):
                s3_index = i + j + 1
                can = False

                if last[j+1]:
                    can = s2_list[i] == s3[s3_index]
                if not can and now[j]:
                    can = s1_list[j] == s3[s3_index]
                now.append(can)
            last = now
        return last[-1]



if __name__ == '__main__':
    wds= Solution()
    print wds.isInterleave('aabcc','dbbca','aadbbbaccc')
