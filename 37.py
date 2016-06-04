class Solution(object):
    def sudoku(self,i,j):
        while self.board[i][j] != '.':
            j += 1
            if j > 8:
                j = 0
                i += 1
                if i > 8:
                    return True

        b = (i/3)*3+j/3

        for num in range(1,10):
            if self.row[i][num]:
                continue
            if self.col[j][num]:
                continue
            if self.block[b][num]:
                continue

            self.row[i][num] = True
            self.col[j][num] = True
            self.block[b][num] = True
            self.board[i][j] = str(num)
            result = self.sudoku(i,j)
            if result:
                return True

            self.board[i][j] = '.'
            self.block[b][num] = False
            self.col[j][num] = False
            self.row[i][num] = False
        return False


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.row = []
        for i in range(9):
            tmp_row = [False for j in range(10)]
            for j in range(9):
                if board[i][j] != '.':
                    tmp_row[int(board[i][j])] = True
            self.row.append(tmp_row)

        self.col = []
        for i in range(9):
            tmp_col = [False for j in range(10)]
            for j in range(9):
                if board[j][i] != '.':
                    tmp_col[int(board[j][i])] = True

            self.col.append(tmp_col)

        self.block = []
        block_row = [0,0,0,3,3,3,6,6,6]
        block_col = [0,3,6,0,3,6,0,3,6]

        for b in range(9):
            tmp_block = [False for i in range(10)]
            for i in range(block_row[b],block_row[b]+3):
                for j in range(block_col[b],block_col[b]+3):
                    if board[i][j] != '.':
                        tmp_block[int(board[i][j])] = True
            self.block.append(tmp_block)

        self.sudoku(0,0)

if __name__ == '__main__':
    wds= Solution()
    tt = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    wds.solveSudoku(tt)
    print tt


