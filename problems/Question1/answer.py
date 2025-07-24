class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #To store rows and columns that contain 0
        row = []
        col = []

        #To find zeroes in the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        #Convert to set to avoid duplicates
        row_set = set(row)
        col_set = set(col)

        #To Zero out Rows
        for i in row_set:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0

        #To Zero out Columns
        for i in range(len(matrix)):
            for j in col_set:
                matrix[i][j] = 0
                
        