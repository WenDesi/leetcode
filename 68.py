class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """


        lines = []
        i = 0
        while i < len(words):
            line = []
            length = 0
            while i < len(words):
                if len(words[i]) == 0:
                    i += 1
                    continue

                if length + len(words[i]) <= maxWidth:
                    line.append(words[i])
                    length += len(words[i]) + 1
                    i += 1
                else:
                    break
            lines.append(line)

        results = []

        for i in range(len(lines)-1):
            tmp = []
            if len(lines[i]) == 1:
                remain = maxWidth - len(lines[i][0])
                results.append(lines[i][0] + ' '*remain)
                continue

            len_remain = len(lines[i]) - 1
            total_len = 0
            for ele in lines[i]:
                total_len += len(ele)
            remain = maxWidth - total_len
            every_space = remain / len_remain
            remain_space = remain - every_space*len_remain

            result = ''
            for j in range(len_remain):
                result += lines[i][j] + ' '*every_space
                if j < remain_space:
                    result += ' '
            result += lines[i][-1]
            results.append(result)

        last_line = lines[-1]
        result = ''
        for j in range(len(last_line)-1):
            result += last_line[j] + ' '
        if len(last_line) > 0:
            result += last_line[-1]
        remain = maxWidth - len(result)
        result += ' '*remain
        results.append(result)
        return results

if __name__ == '__main__':
    wds = Solution()
    print wds.fullJustify(["Here","is","an","example","of","text","justification."],14)
