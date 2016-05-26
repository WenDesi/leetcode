class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) < 1:
            return matrix

        row = [False for i in range(len(matrix))]
        line = [False for i in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    line[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] and line[j]:
                    matrix[i][j] = 0
