class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Initializing empty row and column variables
        row = []
        col = []

        #Finding Which Row and Which Column are zero'd 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)

        #Converting to set for avoiding duplicates
        row_set = set(row)
        col_set = set(col)

        #Zero-ing out the rows
        for i in row_set:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        
        #Zero-ing out the cols 
        for i in range(len(matrix)):
            for j in col_set:
                matrix[i][j] = 0
