class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        count = [0]*26
        wds = [0]*len(s)

        # init some dp table
        for i in range(len(s)-1,-1,-1):
            char = s[i]
            index = dict[char]
            count[index] += 1
            wds[i] = count[index]

        stack = []
        stack_char = []
        result = []
        remain = [0]*26
        for i in range(len(s)):
            char =  s[i]
            index = dict[char]
            remain[index] = wds[i]

            if char in result:
                continue

            if wds[i] == 1:

                for i in range(len(stack)):
                    if stack[i] == index:
                        break
                    if stack[i] < index or remain[stack[i]] == 1:
                        result.append(stack_char[i])
                stack = stack[i+1:]
                stack_char = stack_char[i+1:]
                if char not in result:
                    result.append(char)
                continue
            else:
                if index in stack:
                    continue
                else:
                    try:
                        while index < stack[-1]:
                            stack.pop()
                            stack_char.pop()
                    except:
                        pass
                    stack.append(index)
                    stack_char.append(char)
        result.extend(stack_char)
        return ''.join(result)





if __name__ == '__main__':
    wds= Solution()
    print wds.removeDuplicateLetters("mitnlruhznjfyzmtmfnstsxwktxlboxutbic")