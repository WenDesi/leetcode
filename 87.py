class Solution(object):
    def lettercount(self,s1,s2):
        dict1,dict2={},{}
        for i in range(len(s1)):
            if s1[i] not in dict1:
                dict1[s1[i]] = 1
            else:
                dict1[s1[i]] += 1
            if s2[i] not in dict2:
                dict2[s2[i]] = 1
            else:
                dict2[s2[i]] += 1

        for i in range(len(s1)):
            char  = s1[i]
            try:
                if dict1[char] != dict2[char]:
                    return False
            except:
                return False

        return True


    def recursive(self,s1,s2):
        length = len(s1)

        if length == 1 or s1 == s2:
            return s1 == s2

        if not self.lettercount(s1,s2):
            return False

        for i in range(1,length):
            s1_one = s1[:i]
            s2_one = s2[:i]

            s1_two = s1[i:]
            s2_two = s2[i:]

            one_flag,two_flag = False,False

            if (s1_one,s2_one) in self.dp:
                one_flag = self.dp[(s1_one,s2_one)]
            else:
                one_flag = self.recursive(s1_one,s2_one)

            if (s1_two,s2_two) in self.dp:
                two_flag = self.dp[(s1_two,s2_two)]
            else:
                two_flag = self.recursive(s1_two,s2_two)


            if one_flag and two_flag:
                self.dp[(s1,s2)] = True
                return True

        for i in range(1,length):
            s1_one = s1[:i]
            s2_one = s2[length-i:]

            s1_two = s1[i:]
            s2_two = s2[:length-i]

            one_flag,two_flag = False,False

            if (s1_one,s2_one) in self.dp:
                one_flag = self.dp[(s1_one,s2_one)]
            else:
                one_flag = self.recursive(s1_one,s2_one)

            if (s1_two,s2_two) in self.dp:
                two_flag = self.dp[(s1_two,s2_two)]
            else:
                two_flag = self.recursive(s1_two,s2_two)


            if one_flag and two_flag:
                self.dp[(s1,s2)] = True
                return True
        self.dp[(s1,s2)] = False
        return False



    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.dp = {}

        return self.recursive(s1,s2)

if __name__ == '__main__':
    wds= Solution()
    print wds.isScramble('oatzzffqpnwcxhejzjsnpmkmzngneo','acegneonzmkmpnsjzjhxwnpqffzzto')

