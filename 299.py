class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        secret_dict = {}
        guess_dict = {}

        for s in secret:
            secret_dict[s] = 0
            guess_dict[s] = 0

        for s in guess:
            secret_dict[s] = 0
            guess_dict[s] = 0


        A,B = 0,0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                A += 1
            else:
                secret_dict[secret[i]] += 1
                guess_dict[guess[i]] += 1


        for ele in guess_dict:
            B += min(guess_dict[ele],secret_dict[ele])

        result = '%dA%dB' % (A,B)
        return result

if __name__ == '__main__':
    wds = Solution()
    print wds.getHint("1","2")


