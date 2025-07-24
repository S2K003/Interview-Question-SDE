class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)# Number of Rows 
        n = len(matrix[0])# Number of Columns

        #Default Holder Row and Column
        row = [False] * m
        col = [False] * n

        #Found where the 0 exist
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    #There is a zero present
                    row[i] = True
                    col[j] = True
        
        #Zero out rows
        for i in range(m):
            if row[i] == True:
                for j in range(n):
                    matrix[i][j] = 0

        #Zero out column
        for j in range(n):
            if col[j] == True:
                for i in range(m):
                    matrix[i][j] = 0