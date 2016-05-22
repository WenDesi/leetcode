class Solution(object):
    x_ = [0,0,1,-1]
    y_ = [1,-1,0,0]

    def find(self,word,x,y):
        if len(word) == 0:
            return True

        if self.board[x][y] != word[0]:
            return False

        self.board[x][y] = '-'
        for ii in range(4):
            result = self.find(word[1:],x+self.x_[ii],y+self.y_[ii])
            if result:
                return True
        self.board[x][y] = word[0]
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = []

        for ele in board:
            self.board.append(list(ele))

        margin_head = ['-' for i in range(len(board[0]))]
        margin_tail = ['-' for i in range(len(board[0]))]
        self.board.insert(0,margin_head)
        self.board.append(margin_tail)

        for ele in self.board:
            ele.insert(0,'-')
            ele.append('-')

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                ele = self.board[i][j]
                if ele == word[0]:
                    self.board[i][j] = '-'
                    for ii in range(4):
                        result = self.find(word[1:],i+self.x_[ii],j+self.y_[ii])
                        if result:
                            return True
                    self.board[i][j] = word[0]
        return False




if __name__ == '__main__':
    wds= Solution()
    print wds.exist(["ABCE","SFCS","ADEE"],"ABCCED")