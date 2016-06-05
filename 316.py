class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        count = [0 for i in range(26)]

        for ele in s:
            index = dict[ele]
            count[index] += 1

        for ele in s:
            print count[dict[ele]]


if __name__ == '__main__':
    wds= Solution()
    wds.removeDuplicateLetters("fjzcnmelkfnaliucklvnmke")