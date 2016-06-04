class Solution(object):
    def NQueens(self, x):
        if x >= self.n:
            tt = []
            for i in range(self.n):
                tmp = ['.' for j in range(self.n)]
                tmp[self.result[i]] = 'Q'
                tt.append(''.join(tmp))
            self.wds.append(tt)
            return

        for y in range(self.n):
            left_xie = (x+y)
            right_xie = (y-x) + self.n

            if self.col[y]:
                continue
            if self.left_xie[left_xie]:
                continue
            if self.right_xie[right_xie]:
                continue

            self.result[x] = y
            self.col[y] = True
            self.left_xie[left_xie] = True
            self.right_xie[right_xie] = True
            self.NQueens(x+1)
            self.right_xie[right_xie] = False
            self.left_xie[left_xie] = False
            self.col[y] = False
            self.result[x] = -1

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        self.n = n
        self.row = [ False for i in range(n) ]
        self.col = [ False for i in range(n) ]
        self.left_xie = [ False for i in range(2*n) ]
        self.right_xie = [ False for i in range(2*n) ]
        self.result = [-1 for i in range(n)]
        self.wds = []

        self.NQueens(0)
        return self.wds

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        rr = self.solveNQueens(n)
        return len(rr)