class Trie(object):
    dict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

    def __init__(self):
        self.root = [None for i in range(26)]
        self.root_count = [0 for i in range(26)]
        self.end = False
        self.word = None
        self.count = 0

    def add(self,s):
        s_list = list(s)
        tmp = self
        tmp_root = self.root
        for char in s_list:
            index = self.dict[char]
            if tmp_root[index] == None:
                tmp_root[index] = Trie()
            tmp.root_count[index] += 1
            tmp = tmp_root[index]
            tmp_root = tmp.root

        tmp.word = s
        tmp.end = True
        tmp.count += 1

    def remove(self,s):
        s_list = list(s)
        tmp = self
        tmp_root = self.root
        for char in s_list:

            index = self.dict[char]
            if tmp_root[index] == None:
                return
            stack_head.append(tmp)
            stack_char.append(index)
            if tmp.count == 0:
                del tmp
                return
            tmp = tmp_root[index]
            tmp_root = tmp.root

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie_root = Trie()
        for word in words:
            trie_root.add(word)

        trie_root.remove('eat')
        for i in range(10):
            print i

if __name__ == '__main__':
    wds= Solution()
    print wds.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],["oath","pea","eat","rain"])
